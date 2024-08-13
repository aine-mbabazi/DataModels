from rest_framework.response import Response;
from rest_framework.views import APIView;
from student.models import Student;
from teacher.models import Teacher;
from course.models import Course;
from class_period.models import Class_period;
from classs.models import Classs;
from rest_framework import status;
# from class_model.models import Classroom;
from .serializers import StudentSerializer;
from .serializers import TeacherSerializer
from .serializers import CourseSerializer; 
from .serializers import ClasssSerializer;
from .serializers import Class_periodSerializer;

# from .serializers import ClassPeriodSerializer;
class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name:
            students = students.filter(first_name=first_name)
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        

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
        classrooms = Classs.objects.all()
        serializer = ClasssSerializer(classrooms, many = True)
        return Response(serializer.data)
class Class_periodListView(APIView):
    def get(self,request):
        class_periods = Class_period.objects.all()
        serializer = Class_periodSerializer(class_periods, many = True)
        return Response(serializer.data)
    
class StudentDetailView(APIView):
    def get(self,request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self,request,id):
        student = student.objects.get(id=id)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def enroll(self, Student,course_id):
        course = Course.objects.get(id=course_id)
        Student.courses.add(course)
    
    def post(self,request,id):
        student = Student.objects.get(id=id)
        action = request.data.get("action")
        if action =="enroll":
            course_id = request.data.get(
                "course_id"
            )
            self.enroll(Student,course_id)
        
        return Response(status=status.HTTP_201_CREATED)
    
    def unenroll(self, student, course_id):
        course = Course.objects.get(id=course_id)
        student.courses.remove(course)
        
    def add_to_class(self, student, class_id):
        student_class = Student.objects.get(id=class_id)
        student_class.students.add(student)

    def post(self, request, id):
        student = Student.objects.get(id=id)
        action = request.data.get("action")

        if action == "enroll":
            course_id = request.data.get("course_id")
            self.enroll(student, course_id)
            return Response(status=status.HTTP_201_CREATED)
        
        elif action == "unenroll":
            course_id = request.data.get("course_id")
            self.unenroll(student, course_id)
            return Response(status=status.HTTP_200_OK)
        
        elif action == "add_to_class":
            class_id = request.data.get("class_id")
            self.add_to_class(student, class_id)
            return Response(status=status.HTTP_201_CREATED)
        else:
         return Response(status=status.HTTP_400_BAD_REQUEST)
    

class TeacherDetailView(APIView):
    def get(self,request,id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer.get(teacher)
        return Response(serializer.data)
    
    def put(self,request,id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED
        )
    

    def assign_teacher_to_course(self, teacher_id, course_id):
       
        data = {
            'teacher_id': teacher_id,
            'course_id': course_id
        }
        return self.api_client.post('assign_teacher/course', data)

    def assign_teacher_to_class(self, teacher_id, class_id):
       
        data = {
            'teacher_id': teacher_id,
            'class_id': class_id
        }
        return self.api_client.post('assign_teacher/class', data)
    

class ClasssDetailView(APIView):
    def get(self,request,id):
        classs = Classs.objects.get(id=id)
        serializer = ClasssSerializer.get(classs)
        return Response(serializer.data)
    
    def put(self,request,id):
        classs = Classs.objects.get(id=id)
        serializer = ClasssSerializer(classs,data=request.data)
        if serializer. is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:

            return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,id):
        classs = Classs.objects.get(id=id)
        classs.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
    def create_class_period(self, teacher_id, course_id, class_time):
       
        data = {
            'teacher_id': teacher_id,
            'course_id': course_id,
            'class_time': class_time
        }
        return self.api_client.post('class_periods', data)
    

class CourseDetailView(APIView):
    
    def get(self,request,id):
        course =Course.objects.get(id=id)
        serializer = CourseSerializer.get(id=id)
        return Response(serializer.data)
    
    def put(self,request,id):
        course = Course.objects.get(id=id)
        serializer = CourseSerializer(Course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:

            return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
            

            





