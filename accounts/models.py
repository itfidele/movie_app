from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
# Create your models here.

class User(AbstractUser):
    GENDER = (
        ('Male','Male'),
        ('Female','Female')
    )
    gender=models.CharField(max_length=30,choices=GENDER)
    age=models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='members')


class Movies(models.Model):
    title = models.CharField(max_length=100)
    actors = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    release_date = models.DateField()
    description = models.TextField()
    movie_poster= models.ImageField(upload_to = 'movies')
    url = models.URLField()
    created_at = models.DateTimeField(auto_now=True)
    