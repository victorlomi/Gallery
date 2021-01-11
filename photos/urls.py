from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('photos/<int:photo_id>/', views.photo, name="photos")
]
