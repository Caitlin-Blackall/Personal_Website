from django.db import models

# Create your models here.
class Profile(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    #image = models.FilePathField(path="/about_me/img")
    image = models.ImageField(upload_to='about_me/img')