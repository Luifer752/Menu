from django.urls import path
from .views import CoursesListView, CourseDetailView
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('', CoursesListView.as_view(), name='courses_list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
]
