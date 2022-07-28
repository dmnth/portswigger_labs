#! /usr/bin/env python3

from requests_html import HTMLSession

url = 'https://' + 'www.google.com'

def create_session():
    session = HTMLSession()
    return session 

def get_url(session, url):
    page = session.get(url)
    return page

def post_url(session, url):
    result = session.post(url, headers=headers)

def modify_url(url):
    value = '& echo dicks &'
    url = url.replace('FUZZ', value)
    return url 

def test_can_create_session():
    s = create_session()

def test_can_send_get():
    session = create_session()
    response = get_url(session, url)
    assert(200 == response.status_code)

def test_can_get_sid():
    assert(False)

def test_can_modify_url():
    old_url = url + '/FUZZ'
    new_url = modify_url(url)
    assert(old_url != new_url)

if __name__ = "__main__":

    session = create_session
