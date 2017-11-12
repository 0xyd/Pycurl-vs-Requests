from io import BytesIO
import requests
import pycurl

headers = {}
def header_function(header_line):
    # HTTP standard specifies that headers are encoded in iso-8859-1.
    # On Python 2, decoding step can be skipped.
    # On Python 3, decoding step is required.
    header_line = header_line.decode('iso-8859-1')

    # Header lines include the first status line (HTTP/1.x ...).
    # We are going to ignore all lines that don't have a colon in them.
    # This will botch headers that are split on multiple lines...
    if ':' not in header_line:
        return

    # Break the header line into header name and value.
    name, value = header_line.split(':', 1)

    # Remove whitespace that may be present.
    # Header lines include the trailing newline, and there may be whitespace
    # around the colon.
    name = name.strip()
    value = value.strip()

    # Header names are case insensitive.
    # Lowercase name here.
    name = name.lower()

    # Now we can actually record the header name and value.
    headers[name] = value

def main():
    # Try Requests
    print('Use requests to get Google')
    res = requests.get('https://www.google.com')
    print('check headers')
    print(res.headers)
    print('check content:')
    print(res.text)
    print('-' * 20)
    # Try pycurl
    print('Use pycurl to get Google')
    b = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, 'https://www.google.com')
    c.setopt(c.HEADERFUNCTION, header_function)
    c.setopt(c.WRITEDATA, b)
    c.perform()
    print('check headers:')
    print(headers)
    print('check content:')
    print(b.getvalue())
    print('-' * 20)

if __name__ == '__main__':
    main()


