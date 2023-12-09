from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView

from menu.models import Menu


def main(request):
    menu_list = Menu.objects.filter(parent=None)
    context = {
        "menu_list": menu_list,
    }
    return render(request, 'menu/main.html', context)


class MenuDetailView(DetailView):
    model = Menu
    reverse_lazy

