#! /usr/bin/env python3

import hashlib
import base64

string = 'peter'
cookie_string = '51dc30ddc473d43a6011e9ebba6ca770'

print(cookie_string)
hashed_string = hashlib.md5(string.encode('utf-8')).hexdigest()
print(hashed_string)

tampered_string = base64.b64encode('wiener:51dc30ddc473d43a6011e9ebba6ca770'.encode('ascii'))
print(tampered_string.decode())
