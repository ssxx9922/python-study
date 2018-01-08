from django.db import models

# Create your models here.

class article(models.Model):
    author = models.CharField(max_length=32)
    writetime = models.DateTimeField()
    title = models.CharField(max_length=32)
    text = models.TextField()

    def __str__(self):
        return self.title