from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.first_name + " " + self.last_name
