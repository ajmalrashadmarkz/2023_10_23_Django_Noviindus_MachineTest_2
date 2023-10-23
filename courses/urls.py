from django.urls import path

from .views import (
    ShortTermCourseListView,
    ShortTermCourseDetailView,
    ShortTermCourseDeleteView,
    ShortTermCourseCreateView,  # new
)

urlpatterns = [
    path("<int:pk>/", ShortTermCourseDetailView.as_view(), name="shorttermcourse_detail"),
    path("<int:pk>/delete/", ShortTermCourseDeleteView.as_view(), name="shorttermcourse_delete"),
    path("new/", ShortTermCourseCreateView.as_view(), name="shorttermcourse_new"),  # new
    path("list/", ShortTermCourseListView.as_view(), name="shorttermcourse_list"),
]