from django.db import models
from origin.models import Origin
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=128)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.name
