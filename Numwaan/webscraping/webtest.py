import requests
from bs4 import BeautifulSoup

url = "https://www.lottery.co.th/small"
data = requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
soup = BeautifulSoup(data.text, 'html.parser')

data1 = soup.find_all("button",{"class":"btn-primary"})
data1_list=[]

for item in data1:
    data1_list.append(item.text)

print(data1_list)








##############################
# import requests
# from bs4 import BeautifulSoup

# url = "https://www.expedia.co.th/stories/travel-tips-inspiration/bd01_april17/"
# data = requests.get(url,headers={"User-Agent":"Mozilla/5.0"})
# soup = BeautifulSoup(data.text, 'html.parser')

# data1 = soup.find("h3")
# print(data1)
# data1_list=[]

# for item in data1:
#     data1_list.append(item.text)

# print(data1_list)