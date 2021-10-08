from django.db import models

from django.urls import reverse
from django.utils.text import slugify

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}


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
    time_create = models.DateTimeField(verbose_name="Дата добавления")
    time_update = models.DateTimeField(verbose_name="Дата изменения")
    count_views = models.IntegerField(auto_created=True, default=0, editable=False, verbose_name='Счетчик просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ['-time_create', 'title']

    def get_absolute_url(self):
        return reverse('records:record', kwargs={'slug': self.slug})

    def save_with_slug(self, *args, **kwargs):
        self.slug = slugify(''.join(alphabet.get(w, w) for w in self.title.lower()))
        super(Records, self).save(*args, **kwargs)
