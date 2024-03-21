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
    # profile_pic=models.ImageField(upload_to='profile_images/profile_pic')

class Poll(models.Model):
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question

class PollOptions(models.Model):
    poll = models.ForeignKey(Poll, related_name='options', on_delete=models.CASCADE)
    option_text = models.CharField(max_length=100)

    def __str__(self):
        return self.option_text








    