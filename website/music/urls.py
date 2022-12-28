from django import urls
from django.urls import path
# to connect main urls.py file
from django.contrib import admin
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    path("", views.index, name = "index"),
    # /music/<album_id>/
    path("<album_id>/", views.detail, name = "detail"),
    # /music/<album_id>/favorite
    path("<album_id>/favorite/", views.favorite, name = "favorite"),

]
