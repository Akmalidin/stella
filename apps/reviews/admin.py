from django.contrib import admin
from .models import Reviews

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'created_at')
    search_fields = ('name', 'comment')
    list_filter = ('name', 'comment')


admin.site.register(Reviews, ReviewsAdmin)