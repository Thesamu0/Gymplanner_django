from django.db import models
from django.core import validators

# Create your models here.

class Exercise(models.Model):
    name = models.CharField(max_length=30)
    difficulty_rating = models.IntegerField(default=0,validators=[validators.MaxValueValidator(limit_value=5),validators.MinValueValidator(limit_value=1)])
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name