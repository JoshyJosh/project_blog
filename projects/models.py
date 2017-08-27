from django.db import models
from django.utils.text import slugify
from blog.models import PostCategory

from filer.fields.image import FilerImageField
import os

import re
# Create your models here.


class ProjectCategory(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=4000)
    thumb = FilerImageField(related_name="project_thumbs")
    slug = models.SlugField(blank=True)
    category = models.ManyToManyField(ProjectCategory, default=None, blank=True)
    proj_link = models.CharField(max_length=800, default=None, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Project, self).save(*args, **kwargs)
        if not self.slug:
            slugstring = slugify(self.title)
            similar_slugs = Project.objects.filter(slug__startswith=slugstring)
            if similar_slugs.count() > 0:
                last_slug = similar_slugs.last().slug
                slug_reg = re.search(r'\d+$', last_slug)
                if slug_reg:
                    self.slug = slugstring + "_" + str(int(slug_reg.group(0)) + 1)
                else:
                    self.slug = slugstring + "_1"
            else:
                self.slug = slugstring

        super(Project, self).save()
