from django.contrib import admin
from .models import bookList
# Register your models here.

@admin.register(bookList)
class bookListAdmin(admin.ModelAdmin):
    list_display = ['id', 'bookName', 'authorName', 'bookDescription']