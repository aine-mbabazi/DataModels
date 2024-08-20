from django.db import models

# Create your models here.

class Course(models.Model):
      course_name= models.CharField(max_length =20)
      course_id = models.PositiveSmallIntegerField()
      department = models.CharField(max_length=20)
      course_description = models.TextField()
      class_hours = models.DurationField()
      course_instructor = models.CharField(max_length =20)
      assessment_requirements = models.TextField()
      course_capacity = models.PositiveSmallIntegerField()
      grade_level = models.CharField(max_length=15)
      school_term = models.PositiveSmallIntegerField()
      school_name = models.CharField(max_length =20)

    
      def __str__(self):
        return f"{self.course_name} {self.course_id}"

