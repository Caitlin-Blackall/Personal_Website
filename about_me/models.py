from django.db import models

# Create your models here.
class Profile(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FilePathField(path="/img")