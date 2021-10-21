from django.db import models
from datetime import datetime
# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    topic = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)
    phone = models.TextField(max_length=50)
    car_id = models.IntegerField()
    user_id = models.IntegerField(blank=True)
    
    def __str__(self) -> str:
        return self.email
    