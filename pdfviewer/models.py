from django.db import models

# Create your models here.
class Score(models.Model):
    title = models.CharField(max_length=200)
    pdf_url = models.CharField(max_length=200)
    mei_url = models.CharField(max_length=200)

class Score_Comments(models.Model):
    author = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    date = models.DateTimeField('date published')
    score = models.ForeignKey(Score, on_delete=models.CASCADE)
