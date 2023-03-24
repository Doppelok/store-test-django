from django.db import models


# Create your models here.

class EmailNews(models.Model):
    email = models.EmailField()
    status = models.BooleanField(default=True)
