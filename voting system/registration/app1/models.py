from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
from django.contrib.auth.models import AbstractUser,Group,Permission

class CustomUser(AbstractUser):     
    ROLES = [
        ('admin', 'Admin'),
        ('candidate', 'Candidate'),
        ('voter', 'Voter'),
    ]

    role = models.CharField(max_length=40, choices=ROLES,default='voter')
    profile_pic=models.ImageField(upload_to='profile_images/profile_pic')

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='profile'
    )
    image = models.ImageField(upload_to='pics', default='default.svg')