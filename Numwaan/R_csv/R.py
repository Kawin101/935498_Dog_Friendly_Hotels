# import pandas as pd
# data = pd.read_csv('C:/Users/Thidarat/Documents/GitHub/935498_Dog_Friendly_Hotels/Numwaan/R_csv/Youtube.CSV')

# print("...........")
# print(data.head)
# print("...........")

# import csv
# # เปิดไฟล์ CSV ด้วยคำสั่ง with เพื่อให้สิ้นสุดการใช้งานไฟล์ทันทีที่เสร็จสิ้น
# with open('ไฟล์.csv', newline='') as csvfile:
#     # ใช้ DictReader เพื่ออ่านข้อมูลในรูปแบบของ Dictionary
#     csv_reader = csv.DictReader(csvfile)
    
#     # วนลูปอ่านข้อมูลทีละแถว
#     for row in csv_reader:
#         # ทำอะไรกับข้อมูลที่ได้ เช่น พิมพ์ข้อมูลออกมา
#         print(row)

# Import pandas
# import pandas as pd
# reading csv file 
# df = pd.read_csv("C:/Users/Thidarat/Documents/GitHub/935498_Dog_Friendly_Hotels/Numwaan/R_csv/Youtube.CSV")
# print(df.head)

import csv

with open('C:/Users/Thidarat/Documents/GitHub/935498_Dog_Friendly_Hotels/Numwaan/R_csv/Youtube.CSV',encoding="utf8") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row[0])