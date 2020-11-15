from django.db import models
from .Game import Game


class Question(models.Model):
    name = models.TextField(
        max_length=250,
        verbose_name='Вопрос'
    )
    game = models.ForeignKey(
        Game,
        verbose_name='Игра',
        on_delete=models.CASCADE,
        related_name='game_question'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

