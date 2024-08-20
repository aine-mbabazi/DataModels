from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from teacher.models import Teacher
from course.models import Course
from class_period.models import Class_period
from classs.models import Classs
from rest_framework import status
from .serializers import StudentMinimalSerializer, StudentDetailSerializer
from .serializers import TeacherMinimalSerializer, TeacherDetailSerializer
from .serializers import CourseMinimalSerializer, CourseDetailSerializer
from .serializers import ClasssMinimalSerializer, ClasssDetailSerializer
from .serializers import Class_periodMinimalSerializer, Class_periodDetailSerializer


class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name:
            students = students.filter(first_name=first_name)
        serializer = StudentMinimalSerializer(students, many=True)
        return Response(serializer.data)
  
    def post(self, request):
        serializer = StudentDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StudentDetailView(APIView):
#     def get(self, request, id):
#         student = Student.objects.get(id=id)
#         serializer = StudentDetailSerializer(student)
#         return Response(serializer.data)

#     def put(self, request, id):
#         student = Student.objects.get(id=id)
#         serializer = StudentDetailSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         student = Student.objects.get(id=id)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
class StudentDetailView(APIView):
    def get(self, request, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({"detail": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentDetailSerializer(student)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({"detail": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentDetailSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({"detail": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherMinimalSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherDetailSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherDetailSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseMinimalSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetailView(APIView):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        serializer = CourseDetailSerializer(course)
        return Response(serializer.data)

    def put(self, request, id):
        course = Course.objects.get(id=id)
        serializer = CourseDetailSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClasssListView(APIView):
    def get(self, request):
        classes = Classs.objects.all()
        serializer = ClasssMinimalSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClasssDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClasssDetailView(APIView):
    def get(self, request, id):
        classs = Classs.objects.get(id=id)
        serializer = ClasssDetailSerializer(classs)
        return Response(serializer.data)

    def put(self, request, id):
        classs = Classs.objects.get(id=id)
        serializer = ClasssDetailSerializer(classs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        classs = Classs.objects.get(id=id)
        classs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Class_periodListView(APIView):
    def get(self, request):
        class_periods = Class_period.objects.all()
        serializer = Class_periodMinimalSerializer(class_periods, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Class_periodDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Class_periodDetailView(APIView):
    def get(self, request, id):
        class_period = Class_period.objects.get(id=id)
        serializer = Class_periodDetailSerializer(class_period)
        return Response(serializer.data)

    def put(self, request, id):
        class_period = Class_period.objects.get(id=id)
        serializer = Class_periodDetailSerializer(class_period, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        class_period = Class_period.objects.get(id=id)
        class_period.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


