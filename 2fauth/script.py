#! /usr/bin/env python3

import requests
import re
import sys
import os
from queue import Queue
from thread import ResponseGenerator, RequestsThread


jobs = Queue()


def create_jobs(wordlist):
    if not os.path.exists(os.path.abspath(wordlist)):
        print('Specify wordlist')
        sys.exit()
    else:
        data = open(wordlist, 'r').readlines()
        for digit in data:
            jobs.put(digit)

def make_requests(jobs):
    while not jobs.empty():
        result = ResponseGenerator(20, RequestsThread, jobs)
        yield list(result)

def main():
    results = [] 
    create_jobs('digits_product.txt')
    try:
        for result in make_requests(jobs):
            for el in result:
                print(el)
                if el is not None:
                    results.append(el)
                    if 'Incorrect security code' not in el[0].text:
                        print(el[0].headers, el[1])
                        sys.exit()
    except ValueError as err:
        print('nigger')
        sys.exit()

    return results

if __name__ == "__main__":
    check = main()
    print(len(check))

