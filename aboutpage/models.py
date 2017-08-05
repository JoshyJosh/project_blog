from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class AboutPage(models.Model):
    title = models.CharField(max_length=400)
    content = RichTextField(max_length=4000)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # Only one about page can be published
    def save(self, *args, **kwargs):
        if is_published:

            if len(AboutPage.objects.filter(is_published=True)) != 0:
                is_published = False

        super(AboutPage, self).save()

#   TODO only one about page can be published
#   def save(self, *args, **kwargs):
