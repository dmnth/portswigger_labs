#! /usr/bin/env python3

from requests_html import HTMLSession

url = 'https://' + 'www.google.com'

def create_session():
    session = HTMLSession()
    return session 

def get_url(session, url):
    page = session.get(url)
    return page

def test_can_create_session():
    s = create_session()

def test_can_send_get():
    session = create_session()
    response = get_url(session, url)
    assert(200 == response.status_code)

def test_can_modify_url():
    assert(False)
