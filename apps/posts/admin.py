from django.contrib import admin
from .models import Post, CustomerPost


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')

@admin.register(CustomerPost)
class CustomerPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')