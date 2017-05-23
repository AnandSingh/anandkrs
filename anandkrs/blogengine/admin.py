from blogengine.models import Post, Category
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
