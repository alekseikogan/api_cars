from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


# Марка
class Mark(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Марка'
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        db_index=True,
        verbose_name='URL'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Марка'
        verbose_name_plural = 'Марки'

    def __str__(self):
        return self.name


# Машина
class Car(models.Model):
    mark = models.ForeignKey(
        Mark,
        blank=True,
        on_delete=models.PROTECT,
        related_name='cars',
        verbose_name='Марка',
        help_text='Кузов автомобиля'
    )
    model = models.CharField(
        max_length=100,
        verbose_name='Модель')
    body = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Кузов',
        help_text='Кузов автомобиля'
    )
    description = models.TextField(
        null=True, blank=True, verbose_name='Описание')
    year = models.IntegerField(verbose_name='Год')
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления')

    class Meta:
        ordering = ('mark',)
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return (f'{self.mark} {self.model}')
