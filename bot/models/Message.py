from django.db import models


class Message(models.Model):
    profile = models.ForeignKey(
        to='bot.Profile',
        verbose_name='Профиль',
        on_delete=models.PROTECT,
    )
    text = models.TextField(
        verbose_name='текст'
    )
    create_at = models.DateTimeField(
        verbose_name='время получения',
        auto_now_add=True
    )

    def __str__(self):
        return f'Сообщение {self.pk} от {self.profile}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'



