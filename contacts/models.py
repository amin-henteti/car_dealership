from django.db import models
from datetime import datetime
# Create your models here.

class Contact(models.Model):
    user_id = models.IntegerField(blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.TextField(max_length=50)
    customer_need = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    car_id = models.IntegerField()
    car_title = models.CharField(max_length=100)
    car_price = models.IntegerField()
    created_date = models.DateTimeField(blank=True, default=datetime.now)
    
    
    def __str__(self) -> str:
        return self.email
    