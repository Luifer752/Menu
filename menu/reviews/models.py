from django.db import models
from courses.models import Course
# Create your models here.


class Review(models.Model):

    STAR_CHOICES = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)
    stars = models.IntegerField(choices=STAR_CHOICES)

    def __str__(self):
        return f"{self.course} - {self.stars}"
