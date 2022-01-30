# chat/urls.py
from django.urls import path


from . import views

urlpatterns = [
    path('', views.guess, name='guess'),
    path('guess', views.feeling_need_guesser, name='guess'),
    path('hello', views.hello_world, name='hello_world'),
]