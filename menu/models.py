from django.db import models

from django.db import models
from django.db.models import CheckConstraint, Q, F
from django.db.models.signals import post_save
from django.dispatch import receiver


class MenuItem(models.Model):
    title = models.CharField(max_length=256, unique=True, verbose_name='Название')
    parent = models.ForeignKey('self', null=True, blank=True,
                               related_name='children', on_delete=models.PROTECT, verbose_name='Родитель')
    url = models.CharField(max_length=256, blank=True, null=True, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элементы меню'
        constraints = [
            CheckConstraint(
                check=~Q(id=F('parent')),
                name='check_parent',
            ),
        ]

    def __str__(self):
        return self.title


class Menu(models.Model):
    title = models.CharField(max_length=256, unique=True, verbose_name='Название меню')
    slug = models.SlugField(max_length=256, unique=True, verbose_name='Slug')
    items = models.ManyToManyField(MenuItem, verbose_name='Элементы меню', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
