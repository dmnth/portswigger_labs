#! /usr/bin/env python3

# encodes 

import hashlib
import base64

# Test string-o-cookie and username copied from cookies
test_string = 'd2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw'
test_username = 'wiener'
test_password = 'peter'
# hashed password from test string
cookie_password_hash = '51dc30ddc473d43a6011e9ebba6ca770'

print(f'We know that wiener:peter is transformed somehow to {test_string}')
def compare_hashing_alg(cookie_string, test_password):
    hashed_password = hashlib.md5(test_password.encode('utf-8')).hexdigest()
    if hashed_password == cookie_password_hash:
        print('Password is hashed with MD5')

def hash_md5(wordlist, username):

    passwords = open(wordlist, 'r').readlines()

    with open('hashed_passwords.txt', 'w') as file:
        for pwd in passwords:
            val = pwd.rstrip('\n')
            hashed_val = hashlib.md5(val.encode('utf-8')).hexdigest()
            cookie_value = f'{username}:{hashed_val}'.encode('utf-8')
            base64_cookie = base64.b64encode(cookie_value).decode()
            file.write(base64_cookie + '\n')
        file.close()
    print('All passwords on wordlist are hashed with md5 and encoded with'+\
            ' base64')

def test_output(wordlist):
    with open(wordlist, 'r') as file:
        for element in file:
            if element.rstrip('\n') == test_string:
                print(f'one of result\'s matched with {test_string}')

    file.close()

if __name__ == "__main__":
    compare_hashing_alg(cookie_password_hash, test_password)
    hash_md5('wordlist.txt', test_username) 
    test_output('hashed_passwords.txt')

