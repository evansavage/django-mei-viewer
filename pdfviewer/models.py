from django.db import models

# Create your models here.
class Score(models.Model):
    pdf_url = models.CharField(max_length=200)
    mei_url = models.CharField(max_length=200)
