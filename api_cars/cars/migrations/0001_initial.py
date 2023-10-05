# Generated by Django 2.2.16 on 2023-10-05 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Марка')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Марка',
                'verbose_name_plural': 'Марки',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('body', models.CharField(blank=True, help_text='Кузов автомобиля', max_length=100, verbose_name='Кузов')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('mark', models.ForeignKey(blank=True, help_text='Кузов автомобиля', on_delete=django.db.models.deletion.PROTECT, related_name='cars', to='cars.Mark', verbose_name='Марка')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
                'ordering': ('mark',),
            },
        ),
    ]
