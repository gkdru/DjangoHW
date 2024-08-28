from distutils.command.upload import upload
import imp
from statistics import mode
from django.db import models
from django.contrib.auth.models import User




class UserProfile(models.Model):
    FirstName = models.TextField(max_length=200)
    LastName = models.TextField(max_length=200)
    cv = models.FileField(upload_to='file')
    photo = models.ImageField(upload_to='file')
    id_photo = models.ImageField(upload_to='file')



