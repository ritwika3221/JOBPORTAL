from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
# Create your models here.

class studentuser(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    mobile=models.CharField(max_length=50,default="")
    image=models.ImageField(upload_to='img',default="")
    gender=models.CharField(max_length=10,default="")
    first_name=models.CharField(max_length=50,default="")
    last_name=models.CharField(max_length=50,default="")
    role = models.CharField( max_length=10,default="")
    email=models.CharField(max_length=50,default="")
    upload_resume = models.FileField(upload_to='documents',default="")
    # type=models.CharField(max_length=50,default="student")
    
    
class reqruiteruser(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    mobile=models.CharField(max_length=15,default="")
    image=models.FileField(null=True,default="")
    gender=models.CharField(max_length=10,default="")
    company=models.CharField(max_length=50,default="") 
    first_name=models.CharField(max_length=50,default="")
    last_name=models.CharField(max_length=50,default="") 
    role = models.CharField( max_length=10,default="")
    email=models.CharField(max_length=50,default="")
    # type=models.CharField(max_length=50,default="reqruiter")

class job(models.Model):
    reqruiteruser=models.ForeignKey(reqruiteruser, on_delete=models.CASCADE)
    # startdate=models.DateField(default="",null=True)
    # enddate=models.DateField(null=True,default="")
    title=models.CharField(max_length=50,default="",null=True)
    salary=models.FloatField(max_length=50,default="",null=True) 
    description=models.CharField(max_length=200,default="") 
    expirence=models.CharField(max_length=200,default="") 
    location=models.CharField(max_length=200,default="",null=True) 
    skills=models.CharField(max_length=150,default="")
    date=models.DateTimeField(default=timezone.now)
    # creationdate=models.DateField(default="") 

class jobapplied(models.Model):
    studentuser=models.ForeignKey(studentuser, on_delete=models.CASCADE)
    jobid=models.CharField(max_length=50,default="")
    # jobname=models.CharField(default="", max_length=50)
    date=models.DateTimeField(default=timezone.now)
class contactmodel(models.Model):
    email=models.EmailField(max_length=250)
    phone=models.TextField(max_length=10)
    subject=models.TextField(max_length=500)
    message=models.TextField(max_length=500)