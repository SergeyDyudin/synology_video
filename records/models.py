from django.db import models

from django.urls import reverse


class Records(models.Model):

    CONTENT_TYPES = [
        ('video', 'Видео'),
        ('doc', 'Документ'),
    ]

    def upload_path(self, filename):
        if self.type == 'video':
            return f'records/video/{filename}'
        else:
            return f'records/docs/{filename}'

    title = models.CharField(max_length=70, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    file = models.FileField(upload_to=upload_path, verbose_name="Файл")
    type = models.CharField(max_length=20, choices=CONTENT_TYPES, default='video', verbose_name='Тип контента')
    public = models.BooleanField(default=True, verbose_name="Опубликован")
    slug = models.SlugField(unique=True, blank=False, verbose_name="URL")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    count_views = models.IntegerField(auto_created=True, default=0, editable=False, verbose_name='Счетчик просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def get_absolute_url(self):
        return reverse('record', kwargs={'slug': self.slug})
