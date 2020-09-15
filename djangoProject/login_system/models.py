from django.db import models

class Account(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=70)
    is_active = models.BooleanField(default=True)
    is_valid = models.BooleanField(default=False)

    def __str__(self):
        return self.id