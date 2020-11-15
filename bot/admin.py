from django.contrib import admin

from bot.models import *
from .forms import ProfileAmdinFroms


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    form = ProfileAmdinFroms


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'text', 'create_at']
    list_filter = ['profile', 'create_at']


@admin.register(Game)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Question)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'game']
    list_filter = ['game']


@admin.register(Answer)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'name']
    list_filter = ['question']

