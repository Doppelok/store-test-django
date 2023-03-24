from django.db import models


# Create your models here.

class ContactFeedBack(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    subject = models.CharField(max_length=700)
    message = models.TextField()
