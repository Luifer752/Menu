from django.contrib import admin
from courses.models import Course
from origin.models import Origin
from reviews.models import Review

# Register your models here.

admin.site.register(Course)
admin.site.register(Origin)
admin.site.register(Review)
