from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

from .validators import real_age

User = get_user_model()


class Tag(models.Model):
    tag = models.CharField('Тег', max_length=20)

    def __str__(self):
        return self.tag


class Birthday(models.Model):
    first_name = models.CharField(
        'Имя',
        max_length=20)
    last_name = models.CharField(
        'Фамилия',
        max_length=20,
        blank=True,
        help_text='Необязательное поле')
    birthday = models.DateField(
        'Дата рождения',
        validators=(real_age,))
    image = models.ImageField(
        'Фото',
        blank=True,
        upload_to='birthdays_images')
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        null=True,
        on_delete=models.CASCADE)
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        verbose_name='Теги',
        help_text='Удерживайте Ctrl для выбора нескольких вариантов')

    def get_absolute_url(self):
        return reverse('birthday:detail',
                       kwargs={'pk': self.pk})


class Congratulation(models.Model):
    text = models.TextField(
        'Текст поздравления')
    birthday = models.ForeignKey(
        Birthday,
        on_delete=models.CASCADE,
        related_name='congratulations')
    created_at = models.DateTimeField(
        auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']
