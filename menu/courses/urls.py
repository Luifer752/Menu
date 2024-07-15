from django.urls import path
from .views import CoursesListView, CourseDetailView

# app_name = 'courses'

urlpatterns = [
    path('', CoursesListView.as_view(), name='courses_list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail')
]