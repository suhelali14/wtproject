from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount,Usermode,Products,Recommendation,Cart,cartProduct

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
admin.site.register(Usermode)
admin.site.register(Products)
admin.site.register(Recommendation)
admin.site.register(Cart)
admin.site.register(cartProduct)