from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

import re
# Create your models here.


class PostCategory(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class CodePost(models.Model):
    title = models.CharField(max_length=100, default="foo")
    content = RichTextField(max_length=4000, default="bar")
    date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(PostCategory, default=None, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(CodePost, self).save(*args, **kwargs)
        if not self.slug:
            slugstring = slugify(self.title)
            similar_slugs = CodePost.objects.filter(slug__startswith=slugstring)
            if similar_slugs.count() > 0:
                last_slug = similar_slugs.last().slug
                slug_reg = re.search(r'\d+$', last_slug)
                if slug_reg:
                    self.slug = slugstring + "_" + str(int(slug_reg.group(0)) + 1)
                else:
                    self.slug = slugstring + "_1"
            else:
                self.slug = slugstring

        super(CodePost, self).save()
