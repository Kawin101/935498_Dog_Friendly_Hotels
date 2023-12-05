import requests #รีควล
from bs4 import BeautifulSoup #soup ดึงข้อมูล
import urllib.request #urllib นี้สามารถเข้าถึงข้อมูลและดึงข้อมูลได้ไม่ว่าจะเป็น GET และ POST โดยไลบรารี urllib

url = 'https://www.facebook.com/groups/1388644331636914'
page = urllib.request.urlopen(url)

page.encoding = 'utf-8'
soup = BeautifulSoup(page.content, 'html.parser')


data1 = soup.find_all("span",{"class":"xt0psk2"})
data1_list=[]

for item in data1:
    data1_list.append(item)

print(data1_list)