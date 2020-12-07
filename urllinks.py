import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter count: ')
count = int(count)
position = input('Enter position: ')
position = int(position)
print('Retrieving:',url)

while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tags = tags[position-1]
    url = tags.get('href', None)
    print('Retrieving:',url)
    count = count - 1
