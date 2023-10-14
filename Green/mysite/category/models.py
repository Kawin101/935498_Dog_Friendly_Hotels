from django.db import models

# Create your models here.
class Category(models.Model):
    # unique = True/False คือ กำหนดเงื่อนไขห้ามสร้างชื่อหมวดหมู่ซ้ำกัน
    name = models.CharField(max_length=255, unique=True)

    # แปลงข้อมูล Object ไปแสดงผล
    def __str__(self):
        return self.name
        

