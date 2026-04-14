from django import forms
from .models import Employee, Enrollment, Course, Session

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ["employee", "session", "status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["employee"].label_from_instance = lambda obj: f"{obj.email}"
        self.fields["session"].label_from_instance = lambda obj: f"{obj.course} - {obj.session_date}"

class EnrollmentStatusForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ["status"]
