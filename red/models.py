from django.db import models
from django.db.models import Model

# Create your models here.
class People(models.Model):
    fname= models.CharField(max_length=100)
    lname= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    num= models.CharField(max_length=100)

    def __str__(self):
        return self.fname + "  " + self.lname + " \n " + self.email + " \n " + self.num 
    