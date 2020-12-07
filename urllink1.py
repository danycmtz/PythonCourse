import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
list = []

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
for tag in tags:
#    print('TAG:', tag)
#    print('URL:', tag.get('href', None))
#    print('Contents:', tag.contents[0])
#    print('Attrs:', tag.attrs)
    num = tag.contents[0]
    num = int(num)
    list.append(num)

print('Count',len(list))
print('Sum',sum(list))
