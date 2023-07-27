from django.db import models

# Create your models here 
class Login(models.Model):
    name=models.CharField(max_length=50,default="john")
    email=models.CharField(max_length=50,default="john@gmail.com")
    password=models.CharField(max_length=50,default="john")
    phone=models.CharField(max_length=50,default="john")
class Signup(models.Model):
    fname=models.CharField(max_length=50,default='meruva')
    lname=models.CharField(max_length=50,default='meruva')
    email=models.CharField(max_length=50,default="john@gmail.com")
    password=models.CharField(max_length=50,default="john")
    phone=models.CharField(max_length=50,default="john")
