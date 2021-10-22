from django.db import models
from datetime import datetime
from cars.choices import customer_need_choices
# Create your models here.


class Contact(models.Model):
    user_id = models.IntegerField(blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    customer_need = models.CharField(
        ("Topic"),
        choices=customer_need_choices,
        max_length=250,
    )
    message = models.TextField(blank=True)
    car_id = models.IntegerField()
    car_title = models.CharField(max_length=100)
    car_price = models.IntegerField()
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self) -> str:
        return self.email
