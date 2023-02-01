from operator import truediv
from django.db import models
from django.db.models.signals import pre_save
from django.db.models.fields import TextField
from django.contrib.auth.models import User



# Create your models here.

class Company(models.Model):
    name= models.CharField(max_length=200, null=True)
    id = models.AutoField(primary_key=True)
    contact= models.CharField(max_length=200, null=True)
    address= models.CharField(max_length=200, null=True)
    desc=  models.TextField(max_length=500, null=True)
    userz = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, blank=True)
    added_on= models.DateField()

    def __str__(self):
         return self.name

class Medicine(models.Model):
    id= models.AutoField(primary_key=True)
    company_id= models.ForeignKey(Company , on_delete=models.CASCADE, null=True)
    userz = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, blank=True)
    name= models.CharField(max_length=50, null=True)
    sell_price= models.CharField(max_length=200, null=True)
    buy_price= models.CharField(max_length=200, null=True)
    desc= models.CharField(max_length=200, null=True)
    in_stock= models.CharField(max_length=200, null=True)
    added_on= models.DateField()
    shelf_no= models.CharField(max_length=50,null=True)

    def __str__(self):
         return self.name


class Employee(models.Model):
    id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=200, null=True)
    userz = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, blank=True)
    contact= models.CharField(max_length=200, null=True)
    address= models.CharField(max_length=200, null=True)
    salary= models.IntegerField()
    joining_date= models.DateField()

    def __str__(self):
         return self.name



class Bill(models.Model):
    id=models.AutoField(primary_key=True)
    medicine_id=models.ForeignKey(Medicine,on_delete=models.CASCADE)
    userz = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, blank=True)
    qty=models.IntegerField()
    added_on=models.DateField()
    def __str__(self):
         return str(self.medicine_id)

