# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ["_str_", "data"]
    list_filter = ["data"]
    search_fields = ["titolo","contenuto"]
    prepopulated_fields = {"slug":("titolo",)}

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)