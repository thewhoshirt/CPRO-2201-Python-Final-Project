from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee, Enrollment, Course, Session
from .forms import EmployeeForm, EnrollmentForm, EnrollmentStatusForm

# Create your views here.
def test(request):
    return render(request, "analytics_portal/test.html")


# --------------------
# Employees
# --------------------
def employee_list(request):
    department_filter = request.GET.get('department', '')
    employees = Employee.objects.all()
    departments = Employee._meta.get_field('department').choices

    if department_filter:
        employees = employees.filter(department=department_filter)

    return render(request, "analytics_portal/employee/employee_list.html", {"employees":employees, "departments":departments})

def add_employee(request):
    form = EmployeeForm()

    if request.method == "POST":
        form = EmployeeForm(request.POST,)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
        
    return render(request, "analytics_portal/employee/add_employee.html", {"form":form})

def update_employee(request, id):
    employee = Employee.objects.get(id = id)
    form = EmployeeForm(instance=employee)

    if request.method == "POST":
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    
    return render(request, "analytics_portal/employee/update_employee.html",{"form":form})

def delete_employee(request, id):
    employee = Employee.objects.get(id = id)
    employee.delete()

    return redirect("employee_list")

# --------------------
# Enrollements
# --------------------

def enrollment_list(request):
    status_filter = request.GET.get('status', '')
    enrollments = Enrollment.objects.all()
    status = Enrollment._meta.get_field('status').choices

    if status_filter:
        enrollments = enrollments.filter(status=status_filter)

    return render(request, "analytics_portal/enrollment/enrollment_list.html", {"enrollments":enrollments, "status":status})

def add_enrollment(request):
    form = EnrollmentForm()

    if request.method == "POST":
        form = EnrollmentForm(request.POST,)
        if form.is_valid():
            form.save()
            return redirect("enrollment_list")
        
    return render(request, "analytics_portal/enrollment/add_enrollment.html", {"form":form})

def update_enrollment(request, id):
    enrollment = Enrollment.objects.get(id = id)
    form = EnrollmentForm(instance=enrollment)

    if request.method == "POST":
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect("enrollment_list")
    
    return render(request, "analytics_portal/enrollment/update_enrollment.html",{"form":form})

def employee_enrollment_list(request, id):
    employee = Employee.objects.get(id = id)
    enrollments = Enrollment.objects.filter(employee=employee)
    status_filter = request.GET.get('status', '')
    status = Enrollment._meta.get_field('status').choices

    if status_filter:
        enrollments = enrollments.filter(status=status_filter)

    return render(request, "analytics_portal/enrollment/employee_enrollment_list.html",{"employee":employee,"enrollments":enrollments, "status":status})


def update_status(request, id):
    enrollment = Enrollment.objects.get(id = id)
    form = EnrollmentStatusForm(instance=enrollment)

    if request.method == "POST":
        form = EnrollmentStatusForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect("employee_enrollment_list", id)
    
    return render(request, "analytics_portal/enrollment/update_status.html",{"form":form})

# --------------------
# Courses
# --------------------

def course_list(request):
    courses = Course.objects.all()

    return render(request, 'analytics_portal/course/course_list.html', {'courses':courses})