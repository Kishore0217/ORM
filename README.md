# Ex02 Django ORM Web Application
## Date: 27/10/2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](image.png)



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
models.py

from django.db import models
from django.contrib import admin
class bank(models.Model):
	Name=models.CharField(max_length=10)
	Accno=models.IntegerField(primary_key="Accno")
	Amount=models.FloatField()
	interest=models.FloatField()
	duedate=models.DateField()
class bankAdmin(admin.ModelAdmin):
	list_display=('Name','Accno','Amount','interest','duedate')

admin.py

from django.contrib import admin
from.models import bank,bankAdmin
admin.site.register(bank,bankAdmin)
```



## OUTPUT


![alt text](<Screenshot (2).png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
