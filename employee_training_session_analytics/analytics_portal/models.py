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

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["employee", "session"], 
            )
        ]

    def __str__(self):
        return self.employee