from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Course
from origin.models import Origin
from reviews.models import Review


class CoursesListView(ListView):
    model = Course
    template_name = 'Courses_List.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['origins'] = Origin.objects.all()

        return context


class CourseDetailView(DetailView):
    model = Course
    template_name = "Course_detail.html"
    content_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        context['reviews'] = Review.objects.filter(course=course)
        return context


