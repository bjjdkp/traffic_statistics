# --*-- coding:utf-8 --*--

from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
]