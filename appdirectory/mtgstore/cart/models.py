from django.db import models

# Create your models here.

class Card(models.Model):
    imagelink = models.CharField(max_length=255)
    tcgplayerid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    gatherertext = models.TextField(max_length=255)
    storeprice = models.FloatField()


