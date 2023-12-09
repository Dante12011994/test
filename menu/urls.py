from django.urls import path

from menu.apps import MenuConfig
from menu.views import main, MenuDetailView

app_name = MenuConfig.name

urlpatterns = [
    path('', main, name='main'),  # Главная страница
    path('menu/<int:pk>/', MenuDetailView.as_view(), name='menu_view'),  # Страница просмотра отдельного пункта меню
]
