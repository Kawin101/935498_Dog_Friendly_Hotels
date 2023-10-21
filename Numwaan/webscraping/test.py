import requests
from bs4 import BeautifulSoup
import urllib

url = 'https://travel.trueid.net/detail/rDvYykOdorNR'
page = urllib.request.urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

# con = soup.find_all("h3")
# print(con.encode('utf-8'))

for tags in soup.find_all('h3'):
    print(tags.text.encode('utf-8'))




 
# Can be a list of tags
# tags = ['h1', 'h2', 'h3']
# for tags in soup.find_all(tags):
# for tags in soup.find_all('h3'):
    # print(tags.text.encode('utf-8'))

# a = 'xe0\xb8\x9a\xe0\xb8\xb2\xe0\xb8\x87\xe0\xb9\x81\xe0\xb8\xaa\xe0\xb8\x99 \xe0\xb8\x8a\xe0\xb8\xa5\xe0\xb8\x9a\xe0\xb8\xb8\xe0\xb8\xa3\xe0\xb8\xb5'
# print(a.encoding('utf-8'))