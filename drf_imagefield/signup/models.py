from django.db import models


class Person(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=10)
    profile_image = models.ImageField(default='media/default_image.jpeg')
