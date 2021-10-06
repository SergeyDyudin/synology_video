# Generated by Django 3.2.7 on 2021-10-06 14:58

from django.db import migrations, models
import records.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_views', models.IntegerField(auto_created=True, default=0, editable=False, verbose_name='Счетчик просмотров')),
                ('title', models.CharField(max_length=70, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('file', models.FileField(upload_to=records.models.Records.upload_path, verbose_name='Файл')),
                ('type', models.CharField(choices=[('video', 'Видео'), ('doc', 'Документ')], max_length=20)),
                ('public', models.BooleanField(default=True, verbose_name='Опубликован')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
    ]
