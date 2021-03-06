# Generated by Django 3.1.3 on 2020-11-13 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'сообщение', 'verbose_name_plural': 'сообщения'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='external_id',
            field=models.PositiveIntegerField(unique=True, verbose_name='ID пользователя'),
        ),
    ]
