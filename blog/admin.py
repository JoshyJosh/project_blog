from django.contrib import admin

from .models import CodePost, PostCategory

# Register your models here.

admin.site.register(CodePost)


class CodePostAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/media/tinymceareas.js'
        )
