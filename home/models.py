from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
# Create your models here.
User = get_user_model()


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    fullname=models.TextField()
    phone=models.TextField()
    city=models.TextField()
    zipcode=models.TextField()
    birthdate=models.TextField()
    usermode=models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    name = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user


class Usermode(models.Model):
    user = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    usertype=models.CharField(max_length=20,blank=True)
    def __str__(self):
        return self.user
    def __str__(self):
        return self.username
        
class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    phone=models.TextField()
    name=models.TextField()
    description=models.TextField()
    price=models.TextField()
    ratings=models.TextField()
    review=models.TextField()
    type = models.TextField(blank=True)
    productimg = models.ImageField(upload_to='productimg', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user

class Recommendation(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    electronic=models.TextField()
    cloth=models.TextField()
    watches=models.TextField()
    grocery=models.TextField()
    sports=models.TextField()
  
    
    def __str__(self):
        return self.user


class Cart(models.Model):
    product_id=models.IntegerField()
    user = models.CharField(max_length=100)
    electronic=models.IntegerField()
    cloth=models.IntegerField()
    watches=models.IntegerField()
    grocery=models.IntegerField()
    sports=models.IntegerField()
    
    
    def __str__(self):
        return self.user

class cartProduct(models.Model):
    product_id=models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user