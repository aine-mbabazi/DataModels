from rest_framework import serializers
from student.models import Student
from classs.models import Classs
from class_period.models import Class_period
from course.models import Course
from teacher.models import Teacher
from datetime import date


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = "__all__"

class StudentMinimalSerializer(serializers.ModelSerializer):
   
   full_name = serializers.SerializerMethodField()
   def get_full_name(self, Student):
      return f"{Student.first_name} {Student.last_name}"
   
   class Meta:
      model = Student
      fields = ["id","full_name","email"]

class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student  
        fields = '__all__'  

class ClasssSerializer(serializers.ModelSerializer):
    class Meta:
        model=Classs
        fields="__all__"

class ClasssMinimalSerializer(serializers.ModelSerializer):
   
   class_time = serializers.SerializerMethodField()
   def get_class_time(self, Classs):
      return f"Starts: {Classs.start_time} Ends:{Classs.end_time}"
   
   class Meta:
      model = Classs
      fields = ["course","classroom", "class_time"]

class ClasssDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classs  
        fields = '__all__'  
        
class Class_periodSerializer(serializers.ModelSerializer):
  class Meta:
    model=Class_period
    fields="__all__"

class Class_periodMinimalSerializer(serializers.ModelSerializer):
   
   class_time = serializers.SerializerMethodField()
   def get_class_time(self, Class_period):
      return f"Starts: {Class_period.start_time} Ends:{Class_period.end_time}"
   
   class Meta:
      model = Class_period
      fields = ["course","classroom", "class_time"]

class Class_periodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_period  
        fields = '__all__'  
        

class CoursesSerializer(serializers.ModelSerializer):
 class Meta:
    model=Course
    fields = "__all__"

class CourseMinimalSerializer(serializers.ModelSerializer):
   
   school_direction = serializers.SerializerMethodField()
   def get_school_direction(self, Course):
      return f"In {Course.location}, They teach {Course.course_name}"
   
   class Meta:
      model = Course
      fields = ["instructor_id","school_direction","status"]

class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'  

class TeacherSerializer(serializers.ModelSerializer):
 courses = CoursesSerializer(many = True)
 class Meta:
    model=Teacher
    fields = "__all__"
   

class TeacherMinimalSerializer(serializers.ModelSerializer):
   
   full_name = serializers.SerializerMethodField()
   age = serializers.SerializerMethodField()
   def get_full_name(self, Teacher):
      return f"{Teacher.first_name} {Teacher.last_name}"
   def get_age(self, Teacher):
      today = date.today()
      age = today - Teacher.date_of_birth
      return age
   class Meta:
      model = Teacher
      
      fields = ["id","full_name","age","email"]

class TeacherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__' 