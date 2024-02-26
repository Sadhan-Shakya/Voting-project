from django.db import models

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
