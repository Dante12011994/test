from django.urls import path

from menu.apps import MenuConfig
from menu.views import main

app_name = MenuConfig.name

urlpatterns = [
    path('', main, name='main'),
]
