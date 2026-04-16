from django import forms
from .models import Employee, Enrollment, Course, Session

# adding or updating an employee form
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

# adding an enrollment form
class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ["employee", "session", "status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # defines what shows up in the dropdown menus
        self.fields["employee"].label_from_instance = lambda obj: f"{obj.email}"
        self.fields["session"].label_from_instance = lambda obj: f"{obj.course} - {obj.session_date}"

# enrollment form for only updating status
class EnrollmentStatusForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ["status"]

# adding or updating a Course form 
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

# adding or updating a Course form 
class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = "__all__"

