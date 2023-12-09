from django import template
from django.urls import reverse_lazy, reverse

from menu.models import Menu

register = template.Library()


@register.inclusion_tag("menu/includes/menu_tree.html")
def menu_tree(parent):
    return {'childrens': Menu.objects.filter(parent=parent)}

