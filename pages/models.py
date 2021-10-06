from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=100);
    last_name = models.CharField(max_length=100);
    designation = models.CharField(max_length=100);
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    facebook_link = models.URLField(max_length=100);
    twitterlink = models.URLField(max_length=100);
    create_dta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name #'{0} {1}'.format(self.first_name, self.last_name)
        
