from django.db import models


class Profile(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='ID пользователя',
        unique=True
    )
    name = models.TextField(
        verbose_name='имя пользователя'
    )

    def __str__(self):
        return f'#{self.external_id} {self.name}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

