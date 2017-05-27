from blogengine.models import Category, Tag, Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
