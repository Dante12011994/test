from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100, verbose_name='название пункта меню')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='')
