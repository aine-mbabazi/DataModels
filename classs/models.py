from django.db import models
from student.models import Student

# Create your models here.
class Classs(models.Model):
      class_name= models.CharField(max_length =20)
      class_id = models.PositiveSmallIntegerField()
      course = models.CharField(max_length=20)
      teacher = models.CharField(max_length=20)
      enrollment = models.PositiveSmallIntegerField()
      room_number= models.PositiveSmallIntegerField()
      class_time = models.CharField(max_length=20)
      meeting_days = models.CharField(max_length=40)
      academic_year = models.PositiveSmallIntegerField()
      class_capacity = models.PositiveSmallIntegerField()

      students = models.ManyToManyField(Student)
      

    
      def __str__(self):
        return f"{self.class_name} {self.class_id}"

