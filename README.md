# Ex02 Django ORM Web Application
## Date: 21.04.2025

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![image](https://github.com/user-attachments/assets/77c03f53-bb82-4ca2-bcf1-97dc92368408)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
model.py
from django.db import models
from django.contrib import admin
class bankloan(models.Model):
	Name=models.CharField(max_length=10)
	Accountno=models.IntegerField(primary_key="Accountno")
	Interest=models.FloatField()
	Startdate=models.DateField()
	Email=models.EmailField()
	Mobilenumber=models.IntegerField()
	Amount=models.IntegerField()
	Enddate=models.DateField()

class bankloanAdmin(admin.ModelAdmin):
	list_display=('Name','Accountno','Interest','Startdate','Email','Mobilenumber','Amount','Enddate')

admin.py
 from django.contrib import admin
from .models import bankloan,bankloanAdmin
admin.site.register(bankloan,bankloanAdmin)

```
## OUTPUT


![318910514-9684c294-fc42-4095-adf2-660dcdb62c6a](https://github.com/user-attachments/assets/32258f76-100f-4f56-8791-a1eb6a56a08d)


## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
