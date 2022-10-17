from email.policy import default
from unicodedata import category
from django.db import models
from django.utils.text import slugify

# Create your models here.
class News_and_events(models.Model):
    slug = models.SlugField(default='', null=False)
    title = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=300)
    content = models.CharField(max_length=1000)
    type = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    authors = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    created_at = models.CharField(max_length=10)
    updated_at = models.CharField(max_length=10)

    def save(self, *args, **kwargs ):
        self.slug = slugify(self.title)
        super().save()

