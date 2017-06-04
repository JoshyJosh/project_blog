from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class AboutPage(models.Model):
    title = models.CharField(max_length=400)
    content = RichTextField(max_length=4000)

    def __str__(self):
        return self.title


#   TODO only one about page can be published
#   def save(self, *args, **kwargs):
