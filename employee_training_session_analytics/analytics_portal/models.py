from django.db import models

# Create your models here.
class Employee(models.Model):
    department_choices = [("1", "IT"),("2", "HR"),("3", "Sales"),(4,"Admin"),(5,"Management")]

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(choices=department_choices)

    def __str__(self):
        return self.full_name
    
class Enrollment(models):
    status_choices = [(1,"ENROLLED"),(2,"COMPLETED"),(3,"CANCELLED")]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="enrollments")
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name="enrollments")
    status = models.CharField(choices=status_choices)

    def __str__(self):
        return self.employeeclass Course (models.Model):
    category_choices = {
        '1':'Technical',
        '2':'Security',
        '3':'Soft Skills',
        '4':'Leader Ship',
        '5':'Product Training',
        '6':'Cyber Security',
        '7':'Ethics',
        '8':'Other'

    }

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    duration_minutes = models.IntegerField(choices = category_choices)

    def __str__(self):
        return self.name



class Sessions (models.Model):

    mode_choices = {
        '1':'Online',
        '2':'In-Person'
    }

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session_date = models.DateTimeField()
    instructor_name = models.CharField(max_length=150)
    mode = models.CharField(choices=mode_choices)

    def __str__(self):
        return self.name
        return self.employee
