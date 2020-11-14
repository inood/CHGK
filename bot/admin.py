from django.contrib import admin

from bot.models import Profile, Message
from .forms import ProfileAmdinFroms


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    form = ProfileAmdinFroms


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'text', 'create_at']
    list_filter = ['profile', 'create_at']
    pass
    # def get_queryset(self, request):
    #     return

