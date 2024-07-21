from django import urls

from django.urls import path


from .views import StudentListView
from .views import TeacherListView
from .views import ClasssListView
from .views import CourseListView
from .views import StudentDetailView
from .views import Class_periodListView
from .views import ClasssDetailView
from .views import CourseDetailView
from .views import TeacherDetailView
urlpatterns = [
    path("students/", StudentListView.as_view(), name = "student_list_view"),
    path("teachers/", TeacherListView.as_view(), name = "teacher_list_view"),
    path("courses/", CourseListView.as_view(), name = "course_list_view"),
    path("classs/", ClasssListView.as_view(), name = "classs_list_view"),
    path("class_period/", Class_periodListView.as_view(), name = "class_period_list_view"),
    path("students/<int:id>/",StudentDetailView.as_view(), name="student_detail_view"),
    path("classs/<int:id>/",ClasssDetailView.as_view(),name="classs_list_view"),
    path("courses/<int:id>/",CourseDetailView.as_view(), name="course_list_view" ),
    path("teacher/<int:id>/",TeacherDetailView.as_view(),name="teacher_list_view")


]