from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Origin
from courses.models import Course


class OriginListView(ListView):
    model = Origin
    template_name = "origins.html"
    content_object_name = 'origin'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['origins'] = Origin.objects.all()

        return context


class FilteredByOrigin(ListView):
    model = Origin
    template_name = "filtered_courses.html"
    content_object_name = 'origins'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        origin_id = self.kwargs['pk']
        context['origin_id'] = origin_id
        context['courses'] = Course.objects.filter(origin=origin_id)
        return context

