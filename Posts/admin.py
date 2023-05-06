from django.contrib import admin
from .models import Post

# Register your models here.

# admin.site.register(Post)

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['tittle', 'author']
    list_filter = ["date_created"]

