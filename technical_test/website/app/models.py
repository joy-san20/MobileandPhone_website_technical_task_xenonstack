from django.db import models

# Create your models here.
class user(models.Model):
    objects = None
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name
