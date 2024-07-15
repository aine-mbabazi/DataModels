from rest_framework.response import Response;
from rest_framework.views import APIView;
from student.models import Student;
from teacher.models import Teacher;
from course.models import Course;
from classs.models import Class;
# from class_model.models import Classroom;
from .serializer import StudentSerializer;
from .serializer import TeacherSerializer
from .serializer import CourseSerializer;
from .serializer import ClasssSerializer;
# from .serializers import ClassPeriodSerializer;
class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)
class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
class CourseListView(APIView):
    def get(self,request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many = True)
        return Response(serializer.data)
class ClasssListView(APIView):
    def get(self,request):
        classrooms = Class.objects.all()
        serializer = ClasssSerializer(classrooms, many = True)
        return Response(serializer.data)
# class ClassPeriodListView(APIView):
#     def get(self,request):
#         classPeriods = ClassPeriod.objects.all()
#         serializer = ClassPeriodSerializer(classPeriods, many = True)
#         return Response(serializer.data)