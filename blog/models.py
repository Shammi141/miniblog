from django.db import models

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=200)
    author= models.CharField(max_length=200)
    desc= models.TextField()

class Feedback(models.Model):
    name= models.CharField(max_length=200)
    email= models.EmailField()
    address=models.CharField(max_length=200)
    message= models.TextField()

    
    