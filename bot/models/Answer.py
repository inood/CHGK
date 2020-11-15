from django.db import models
from .Question import Question


class Answer(models.Model):
    name = models.CharField(
        max_length=250, 
        verbose_name='Ответ на вопрос',
        unique=True
    )
    question = models.ForeignKey(
        Question,
        verbose_name='Вопрос',
        on_delete=models.CASCADE,
        related_name='answer_question'

    )

    def __str__(self):
        return f'{self.question}: {self.name}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
