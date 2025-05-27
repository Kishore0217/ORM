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
