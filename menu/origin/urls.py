from django.urls import path
from .views import OriginListView, FilteredByOrigin


urlpatterns = [
    path('', OriginListView.as_view(), name='origins'),
    path('<int:pk>/', FilteredByOrigin.as_view(), name='filtered_courses')
]