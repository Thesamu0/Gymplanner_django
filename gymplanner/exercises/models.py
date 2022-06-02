from django.db import models
from django.core import validators

# Create your models here.
class Workout(models.Model):
    name = models.CharField(max_length=30)
    rest_time = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField(max_length=30)    
    description = models.CharField(max_length=500)
    workout = models.ForeignKey(Workout,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
