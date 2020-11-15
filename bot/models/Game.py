from django.db import models


class Game(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name='Название игры',
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
