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



url = 'https://travel.trueid.net/detail/rDvYykOdorNR'
page = urllib.request.urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

# con = soup.find_all("h3")
# print(con.encode('utf-8'))

for tags in soup.find_all('h3'):
    print(tags.text)

for ta in soup.find_all('ul'):
    print(ta.text)