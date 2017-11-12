import pycurl
import requests
from io import BytesIO
from http.cookies import BaseCookie

def decode_cookie(raw_cookie):
    cookie = BaseCookie()
    cookie.load(raw_cookie)
    decoded_cookie = {}
    for c, v in cookie.items():
        decoded_cookie[c] = v.value
    return decoded_cookie

def requests_cookie_get():
    s = requests.session()
    decoded_cookie = decode_cookie('PUT ur raw cookie here.')
    res = s.get('https://www.google.com.tw/', cookies=decoded_cookie)
    res = s.get('https://www.google.com.tw/')
    print(res.text)

def requests_pycurl_get():
    b = BytesIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, 'https://www.google.com.tw/')
    c.setopt(pycurl.COOKIE, 'Put Ur RAW Cookie here')
    c.setopt(pycurl.WRITEDATA, b)
    c.perform()

def main():
    requests_cookie_get()
    requests_pycurl_get()

if __name__ == '__main__':
    main()