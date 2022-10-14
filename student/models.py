from django.db import models
from credentials.models import CustomUser


class Student(models.Model):
    admin = models.OneToOneField()
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone_number = models.TextField()
    email = models.EmailField(unique=True)
    birth_certificate = models.FileField(upload_to='images')
    national_id_file = models.FileField(upload_to='images')
