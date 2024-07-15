from django.db import models
# from course.model import course
# from Class.model import Class
# Create your models here.

class Teacher(models.Model):
      first_name = models.CharField(max_length =20)
      last_name = models.CharField(max_length=20)
      gender = models.CharField(max_length=20)
      nationality= models.CharField(max_length=20)
      email = models.EmailField()
      date_of_joining = models.DateField()
      teacher_id= models.PositiveSmallIntegerField()
      course = models.CharField(max_length=20)
      department = models.CharField(max_length=20)
      bank_account_number = models.CharField(max_length = 16)
      # course =  models.OneToOneRel()  
      # Class = models.ForeignKey()
         

    
      def __str__(self):
        return f"{self.first_name} {self.last_name}"
