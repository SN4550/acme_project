from django.db import models
from django.urls import reverse

from .validators import real_age


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

    def get_absolute_url(self):
        return reverse('birthday:detail',
                       kwargs={'pk': self.pk})
