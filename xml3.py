import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

lst = []
address = input('Enter location: ')

if len(address) < 1: quit

print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
counts = tree.findall('.//count')
comments = tree.findall('comments/comment')

for comment in comments:
    count = (comment.find('count').text)
    count = int(count)
    lst.append(count)

print('Count:',len(counts))
print('Sum:',sum(lst))
