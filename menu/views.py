from django.shortcuts import render

from menu.models import Menu


def main(request):
    menu_list = Menu.objects.filter(parent=None)
    context = {
        "menu_list": menu_list,
    }
    return render(request, 'menu/main.html', context)
