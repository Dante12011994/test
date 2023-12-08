from django import template

from menu.models import Menu

register = template.Library()


@register.inclusion_tag("menu/includes/menu_tree.html")
def menu_tree(cate):
    return {'childrens': Menu.objects.filter(parent=cate)}
