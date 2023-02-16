from django.db import models
from django.urls import reverse


class Albom(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название альбома')
    date = models.DateField(verbose_name='Дата создания')
    picture = models.ImageField(verbose_name='Обожка')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ['date']

    def get_absolute_url(self):
        return reverse('albom_view', kwargs={'albom_id': self.pk})


class Photo(models.Model):
    picture = models.ImageField(verbose_name='Фотография')
    albom_id = models.ForeignKey('Albom', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Альбом')

    class Meta:
        verbose_name = 'Фотографию'
        verbose_name_plural = 'Фотографии'
        ordering = ['-pk']


class AboutMe(models.Model):
    picture = models.ImageField(verbose_name='Изображение')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст блога')
    price = models.IntegerField(verbose_name='Стоимость', default=1000)

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуга'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('DetatilBlog', kwargs={'blog_id': self.pk})
