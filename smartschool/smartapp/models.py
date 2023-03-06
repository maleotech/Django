from django.db import models
import datetime

# Create your models here.
class Activity(models.Model):
    image = models.ImageField(upload_to='images/')
    is_display = models.BooleanField(default=False)
    created_date = models.DateField(default=datetime.date.today)

class Alumni(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    quote = models.TextField()
    is_display = models.BooleanField(default=False)
    created_date = models.DateField(default=datetime.date.today)

    