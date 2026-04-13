from django import forms
from .models import Employee, Enrollment, Course, Session

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"