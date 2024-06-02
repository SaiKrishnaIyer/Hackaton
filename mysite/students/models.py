from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female")
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, blank=True)
    email_id = models.EmailField(max_length=254, unique=True)
    student_gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    student_address = models.TextField(max_length=2000)  
    student_department = models.ManyToManyField('Department')  
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20, blank=True)

class Department(models.Model):  
    department_name = models.CharField(max_length=30)

