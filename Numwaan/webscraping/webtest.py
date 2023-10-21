import requests
from bs4 import BeautifulSoup

# url = "https://www.dogthailand.net/small"
# data = requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
# print(data.text.encode("utf-8")) im_Celebrity_News
url = "https://www.lottery.co.th/small"
data = requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
soup = BeautifulSoup(data.text, 'html.parser')

data1 = soup.find_all("button",{"class":"btn-primary"})
data1_list=[]

for item in data1:
    data1_list.append(item.text)

print(data1_list)