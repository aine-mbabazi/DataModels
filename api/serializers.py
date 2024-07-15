from rest_framework import serializers

from student.models import Student
from classs.models import Classs
from teacher.models import Teacher
from course.models import Course

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class ClasssSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classs
        fields = "__all__"

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"