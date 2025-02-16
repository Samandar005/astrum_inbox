from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('from_email', 'to_email', 'subject', 'user', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('from_email', 'to_email', 'subject', 'message')
    ordering = ('-created_at',)


admin.site.register(Message, MessageAdmin)
