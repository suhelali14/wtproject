from django.contrib import admin
from django.urls import path
from home import views
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('about', views.about,name='about'),
    path('faq', views.faq,name='faq'),
    path('search', views.search,name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('signup', views.signup,name='signup'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),
    path('signuppr', views.signuppr,name='signuppr'),
    path('loginpr', views.loginpr,name='loginpr'),
    path('provider', views.provider,name='provider'),
    path('upload', views.upload,name='upload'),
    path('search', views.search, name='search'),
    path('services', views.services,name='services'),
    path('cart', views.cart,name='cart'),
    path('follow', views.follow, name='follow'),
    path('upload_post', views.upload_post,name='upload_post'),
    
]