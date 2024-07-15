from django.db import models

# Create your models here.
# from student.models import Student

# Create your models here.
class class_period(models.Model):
     start_time = models.TimeField()
     end_time = models.TimeField()
     class_room = models.CharField(max_length= 20)
     day_of_week = models.CharField(max_length = 20)
     teacher = models.CharField(max_length = 20)
     subject = models.CharField(max_length =20)
     is_cancelled = models.BooleanField()
def __str__(self):
        return f"{self.start_time} {self.end_time}"
