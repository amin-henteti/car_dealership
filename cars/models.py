from django.db import models
from django.db.models.enums import Choices
from django.utils.translation import to_locale
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from .choices import (
    state_choices,
    features_choices,
    integer_choices,
    year_choices,
    availibility_choices,
)

# Create your models here.

MAX_NUMBER_VIEWS = 4  # 4 is the total number of views images that can be associated to a car as seen below


class Car(models.Model):
    title = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to="Cars/%d-%m-%Y/")
    views_images_1 = models.ImageField(upload_to="Cars/%d-%m-%Y/", blank=True)
    views_images_2 = models.ImageField(upload_to="Cars/%d-%m-%Y/", blank=True)
    views_images_3 = models.ImageField(upload_to="Cars/%d-%m-%Y/", blank=True)
    views_images_4 = models.ImageField(upload_to="Cars/%d-%m-%Y/", blank=True)
    provinance = models.CharField(choices=state_choices, max_length=100)
    location = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    year = models.IntegerField(("year"), choices=year_choices)
    price = models.IntegerField()
    miles = models.IntegerField()
    condition = models.CharField(max_length=250)

    description = RichTextField()
    features = MultiSelectField(choices=features_choices, max_length=200)

    body_style = models.CharField(max_length=200)
    engine = models.CharField(max_length=200)
    transmission = models.CharField(max_length=200)
    doors = models.IntegerField(("doors"), choices=integer_choices(2, 6))
    passengers = models.IntegerField(
        ("number of passengers"),
        choices=integer_choices(2, 8),
        help_text="Enter the number of passengers",
    )
    fuel_type = models.CharField(
        ("Fuel"),
        choices=(("Essence", "Essence"), ("Gaz", "gaz"), ("Electric", "Electric")),
        max_length=50,
    )
    availibility = models.CharField(
        ("availibility"), choices=availibility_choices, max_length=100
    )
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title + " " + self.model
