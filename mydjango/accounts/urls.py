from django.urls import path, include
from django.urls import  path
from .import views
urlpatterns = [
    path('register',views.test,name='register'),
]
