from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Charity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(max_length=200)

    tags = TaggableManager()

    def __str__(self):
        return self.name