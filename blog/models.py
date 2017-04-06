from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.


class PostCategory(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class CodePost(models.Model):
    codepost_title = models.CharField(max_length=100)
    codepost_content = RichTextField(max_length=4000)
    codepost_date = models.DateTimeField(default=timezone.now())
    codepost_category = models.ManyToManyField(PostCategory)

    def __str__(self):
        return self.codepost_title
