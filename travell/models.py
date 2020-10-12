from django.db import models

# Create your models here.
class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    des = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
class Place(models.Model):
    
    city = models.CharField(max_length=100)
    price = models.IntegerField()

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    feedback = models.TextField()

    
    

    
    