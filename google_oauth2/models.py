from django.db import models

# Create your models here.


class GoogleTokens(models.Model):
    refresh_token = models.CharField(max_length=150)
