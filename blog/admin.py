from django.contrib import admin
from django.db import models
from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import CodePost, PostCategory

# Register your models here.


"""
class CodePostAdminForm(forms.ModelForm):
    codepost_content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = CodePost

class CodePostAdmin(admin.ModelAdmin):
    form = CodePostAdminForm



admin.site.register(CodePost, CodePostAdmin) """

admin.site.register(CodePost)
