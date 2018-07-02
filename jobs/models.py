from django.db import models

# Model for Previous works to show them in Portfolio

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
