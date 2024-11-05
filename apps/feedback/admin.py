from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'message')
    search_fields = ('name', 'phone_number', 'email')
    list_filter = ('name', 'phone_number')
admin.site.register(Feedback, FeedbackAdmin)