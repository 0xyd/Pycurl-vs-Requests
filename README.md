# Pycurl-vs-Requests
A cheatsheet for comparison between pycurl and requests.

All the example code are run on Python 3+.

## Why do we do the Comparison?
*requests* is popular among Python developers because of its human-friendly api.
*pycurl*, on the other hand, is hard-coding but with better performance.

From the view of functionality, *requests* is dedicated to *HTTP protocol*;
*pycurl*, instead, supports various protocols like *HTTP*, *SMTP*, *FTP* and so forth.

We do the comparison over the HTTP methods between two libraries especially for the apis both provide.

## How to Contribute?
Feel free to contribute your knowledge of these two libraries.
Just edit the *Functionality Comparison* part in the README.md file as the following format:
### Functionality Name
The description of functionality comparison result.
requests:
```python
    print('Here is your example code of requests')
```
pycurl:
```python
    print('Here is your example code of pycurl')
```

## Functionality Comparison 
### Get
Requests provides a simple way to conduct Http GET; 
In contrast, pycurl's method is not as friendly as requests'.

requests:
```python
    # Send the requests
    import requests
    res = requests.get('https://www.google.com')

    # Get the result
    res.status_code  # 200
    res.encoding     # 'Big5'
```
pycurl:
```python
    # Send the requests
    import pycurl
    from io import BytesIO
    b = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, 'https://www.google.com')
    c.setopt(c.WRITEDATA, b)
    c.perform() 
    c.close()

    # Get the result
    c.getinfo(pycurl.HTTP_CODE) # 200
    c.getinfo(pycurl.CONTENT_TYPE) # 'text/html; charset=Big5'
```

### Get Header info of response
requests has handle headers with an very elegant way.
If you want to retreive headers information, a parsing function must be used.

requests:
```python
    res.headers
```

pycurl:
```python
    # Header function is used to parse the header from the response
    headers = {}
    def header_function(header_line):
        header_line = header_line.decode('iso-8859-1')
        if ':' not in header_line:
            return
        name, value = header_line.split(':', 1)
        name = name.strip()
        value = value.strip()
        name = name.lower()
        headers[name] = value
    c = pycurl.Curl()
    c.setopt(pycurl.URL, 'https://www.google.com')
    c.setopt(pycurl.HEADERFUNCTION, header_function)
    c.perform()
    print(headers)
```

### Set User-Agent 
requests:
```python
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    res = requests.get('https://www.google.com', headers=headers)
```

pycurl:
```python
    c = pycurl.Curl()
    c.setopt(pycurl.HTTPHEADER, [
        'accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-language:en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4,zh-CN;q=0.2'])
    # Cookie is needed to view google.com.
    c.setopt(pycurl.COOKIEFILE, "") 
    c.setopt(pycurl.URL, 'https://www.google.com')
    c.setopt(pycurl.USERAGENT, 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
    c.perform() 
```

### Post
requests:
```python
    res = requests.post('https://httpbin.org/post', data={'user': 'yudazilian', 'password': '12345'})
```
pycurl:
```python
    c = pycurl.Curl()
    c.setopt(pycurl.URL, 'https://httpbin.org/post')
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.HTTPPOST, [('user', 'yudazilian'), ('password', '12345')])
    c.perform()
```

### Cookie
Requests' cookie accepts dict-like object; Pycurl however, uses the raw string.
Besides, pycurl.Curl() function creates a session object just as what requests.session did.

requests:
```python
    s = requests.session()
    s.get('', cookies={'From': 'Ur Browser'})
```

pycurl:
```python
    c = pycurl.Curl()
    c.setopt(pycurl.URL, '')
    c.setopt('https://www.google.com', 'Raw Cookie String')
```

### Set Socks Proxy
Surprisingly, Pycurl's proxy setting is as simple as requests. 

requests:
```python
    proxies = {
        'http':  'socks5://localhost:9050',
        'https': 'socks5://localhost:9050')
    }
    requests.get('https://httpbin.org/post', proxies=proxies)
```

pycurl:
```python
    c = python.Curl()
    c.setopt(pycurl.PROXY, 'socks5://localhost')
    c.setopt(pycurl.PROXYPORT, 9050)
    c.perform()
```

## Lisence
MIT
