from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    email = models.EmailField()
    alamat = models.CharField(max_length=100, null=True, blank=True)
    nisn = models.CharField(max_length=10, default='0')
    phone_number = models.IntegerField(null=True, blank=True)
    kelas = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    
    