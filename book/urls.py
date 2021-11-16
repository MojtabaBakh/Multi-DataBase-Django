
from django.contrib import admin
from django.urls import path , include
from .views import Booklist









urlpatterns = [
    path('list/', Booklist ),
    
    
]
