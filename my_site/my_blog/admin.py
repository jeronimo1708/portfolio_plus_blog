from django.contrib import admin

from .models import *

class PostAdmin(admin.ModelAdmin):
    # Have to be same as attributes in model classes
    list_filter = ("author", "tags", "date_updated")
    list_display = ("title", "author", "date_updated")
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
