'''
    Performance Comparison between requests and pycurl
'''
import time
import requests
import pycurl
from io import BytesIO

def pycurl_get():
    b = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, 'https://httpbin.org/ip')
    c.setopt(c.WRITEDATA, b)
    c.perform()
    c.close()
    body = b.getvalue()
    print('pycurl_get: %s' % body.decode('utf8'))

def requests_get():
    r = requests.get('https://httpbin.org/ip')
    print('requests_get: %s' % r.text)

def main():
    start_time = time.time()
    for i in range(100):
        requests_get()
    end_time = time.time()
    request_time = end_time - start_time
    
    start_time = time.time()
    for i in range(100):
        pycurl_get()
    end_time = time.time()
    pycurl_time = end_time - start_time

    print('The requests_get takes %f' % request_time)
    print('The pycurl_get takes %f' % pycurl_time)


if __name__ == '__main__':
    main()    
