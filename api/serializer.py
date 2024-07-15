from rest_framework import serializer

from student.models import Student
from classs.models import Class
from teacher.models import Teacher
from course.models import Course

class StudentSerializer(serializer.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class CourseSerializer(serializer.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class ClasssSerializer(serializer.ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"

class TeacherSerializer(serializer.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"