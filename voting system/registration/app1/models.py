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
    def save(self, *args, **kwargs):
        UserModel.objects.create(
            username=self.username,
            email=self.email,
            role=self.role
        )
        super().save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='profile'
    )
    image = models.ImageField(upload_to='pics', default='default.svg')

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    total_vote = models.IntegerField(default=0)
    voters = models.ManyToManyField(User, blank=True)
    
    def __str__(self):
        return self.title
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='category_votes')
    

class CategoryItem(models.Model):
    title = models.CharField(max_length=200)
    total_vote = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    voters = models.ManyToManyField(User, blank=True)

    
    def __str__(self):
        return self.title
    
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL)

    
class UserModel(models.Model): #for crud operation making a table usermodel for inside email all
    username = models.CharField(max_length=60)
    email = models.CharField(max_length=100)  # Assuming email can be stored as a string
    role = models.CharField(max_length=100)