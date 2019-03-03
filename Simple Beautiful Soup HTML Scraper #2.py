import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input('Enter Url:')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)
# print soup
count = int(input('Enter count: '))+1
position = int(input('Enter position: '))


tags = soup('a')
# next line gets count tags starting from position
my_tags = tags[position: position+count]
tags_lst = [] # empty list of anchor tags
for tag in my_tags:
    needed_tag = tag.get('href', None)
    tags_lst.append(needed_tag)
print(tags_lst)
