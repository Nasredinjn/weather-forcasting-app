from django.urls import path
from .views import *
urlpatterns = [
    path('',weather_view,name='weather_view')
]