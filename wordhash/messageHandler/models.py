from django.db import models

class MessageHash(models.Model):
    message = models.CharField(max_length=500, unique=True)
    hash = models.CharField(max_length=100, unique=True, primary_key=True)
