from django.db import models
from django.utils import timezone

# Create your models here.


class PostCategory(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class CodePost(models.Model):
    codepost_title = models.CharField(max_length=100)
    codepost_content = models.TextField
    codepost_date = models.DateTimeField(default=timezone.now())
    codepost_category = models.ManyToManyField(PostCategory)

    def __str__(self):
        return self.codepost_title
