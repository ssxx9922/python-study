from django.db import models

# Create your models here.

class person(models.Model):
    nikename = models.CharField(max_length=16,default='kk')
    sex = models.CharField(max_length=5,default='man') #male 男  madam 女
    phone = models.CharField(max_length=12)
    introduce = models.TextField()
    birth = models.DateField()

    def __str__(self):
        return self.nikename

