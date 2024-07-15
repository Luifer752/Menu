from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Review


class ReviewDetailView(DetailView):
    model = Review
    template_name = "Course_detail.html"
    content_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        context['reviews'] = Review.objects.filter(course=course)
        return context


def review_list(request):
    review = Review.objects.all()
    context = {'review': review}
    return render(request, 'reviews_list.html', context)

