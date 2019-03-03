from urllib.request import urlopen
from bs4 import BeautifulSoup


url = input('Enter - ') # user enter URL
html = urlopen(url,).read() # open then reads contents of URL
soup = BeautifulSoup(html, "html.parser") # Parses content of html to be used with Python
sum = 0
count = 0
# Retrieve all of the anchor tags
tags = soup('span') 
for tag in tags:
    # Look at the parts of a tag
    num = float(tag.contents[0])
    # print numbers
    sum = sum + num
    count = count + 1
print(sum)
print(count)
