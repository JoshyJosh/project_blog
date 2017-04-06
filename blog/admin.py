from django.contrib import admin
from django.db import models
from django import forms

from .models import CodePost, PostCategory

# Register your models here.

admin.site.register(CodePost)


class CodePostAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})},}

    class Media:
        js = (
            '/media/ckeditor/ckeditor/ckeditor.js'
        )
