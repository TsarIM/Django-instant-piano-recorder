from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('songs/', views.create_song, name='create_song'),
]