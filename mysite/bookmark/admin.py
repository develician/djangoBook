from django.contrib import admin

# Register your models here.
from bookmark.models import BookMark


class BookMarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

admin.site.register(BookMark, BookMarkAdmin)