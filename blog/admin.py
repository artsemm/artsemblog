from blog.models import Post
from django.contrib import admin
from markdownx.widgets import AdminMarkdownxWidget

from django.db import models


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    list_display = ('title', 'category', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)