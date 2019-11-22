from django.db import models
from django.conf import settings
class doctor(models.Model):
    username = models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    email=models.EmailField(max_length=254,default='null')
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    city=models.CharField(max_length=30)
    special=models.CharField(max_length=30)
    
# Create your models here.
class ngo(models.Model):
    username = models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    email=models.EmailField(max_length=254,default='null')
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    text=models.TextField()

class patient(models.Model):
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=10)
    dis=models.TextField()
    phone=models.CharField(max_length=10)

class event(models.Model):
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=10)
    venue=models.CharField(max_length=30)
    org_id=models.ForeignKey(ngo,on_delete=models.CASCADE)
    nod=models.IntegerField()
    date=models.DateField()

class regis(models.Model):
    evid=models.ForeignKey(event,on_delete=models.CASCADE)
    doid=models.ForeignKey(doctor,on_delete=models.CASCADE)




