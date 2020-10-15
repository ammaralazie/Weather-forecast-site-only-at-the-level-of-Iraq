from django.db import models
import datetime
class City(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name





# Create your models here.
