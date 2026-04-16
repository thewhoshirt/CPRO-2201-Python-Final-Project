from django.shortcuts import render, redirect
from .models import Employee, Enrollment, Course, Session
from .forms import EmployeeForm, EnrollmentForm, EnrollmentStatusForm

# Create your views here.
def home(request):
    return render(request, "analytics_portal/global_layout.html")

# --------------------
# Analytics
# --------------------
def analytics(request):
    page_filter = request.GET.get('page','')

    # Department Participation
    if page_filter == "1":









        return render(request, "analytics_portal/analytics/analytics.html", {"page": page_filter})
    
    # Employee Training Transcript
    elif page_filter == "2":
        # gets employees for the dropdown and the result if one is chosen
        employees = Employee.objects.all()
        employee_filter = request.GET.get('employee', '')

        # if an employee has been selected, get their data
        if employee_filter:
            employee = Employee.objects.get(id=employee_filter)
            enrollments = Enrollment.objects.filter(employee=employee)

            return render(request, "analytics_portal/analytics/analytics.html", {"page": page_filter, "employees":employees, "employee":employee, "enrollments":enrollments})

        return render(request, "analytics_portal/analytics/analytics.html", {"page": page_filter, "employees":employees})
    

    return render(request, "analytics_portal/analytics/analytics.html", {"page": ""})

# --------------------
# Employees
# --------------------
def employee_list(request):
    # gets departments for the dropdown and the result if one is chosen
    department_filter = request.GET.get('department', '')
    departments = Employee._meta.get_field('department').choices

    employees = Employee.objects.all()

    # filters employees if a specific department has been chosen
    if department_filter:
        employees = employees.filter(department=department_filter)

    return render(request, "analytics_portal/employee/employee_list.html", {"employees":employees, "departments":departments})

def add_employee(request):
    # create the form
    form = EmployeeForm()

    # if the form has been completed, saves employee and returns to list page
    if request.method == "POST":
        form = EmployeeForm(request.POST,)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
        
    return render(request, "analytics_portal/employee/add_employee.html", {"form":form})

def update_employee(request, id):
    # gets the employee from the id and create the form
    employee = Employee.objects.get(id = id)
    form = EmployeeForm(instance=employee)

    # if the form has been completed, saves employee and returns to list page
    if request.method == "POST":
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    
    return render(request, "analytics_portal/employee/update_employee.html",{"form":form})

def delete_employee(request, id):
    # deletes employee from the id
    employee = Employee.objects.get(id = id)
    employee.delete()

    return redirect("employee_list")

# --------------------
# Enrollments
# --------------------

def enrollment_list(request):
    # gets status for the dropdown and the result if one is chosen
    status_filter = request.GET.get('status', '')
    status = Enrollment._meta.get_field('status').choices

    enrollments = Enrollment.objects.all()

    # filters enrollments by status if one is chosen
    if status_filter:
        enrollments = enrollments.filter(status=status_filter)

    return render(request, "analytics_portal/enrollment/enrollment_list.html", {"enrollments":enrollments, "status":status})

def add_enrollment(request):
    # create form
    form = EnrollmentForm()

    # if the form has been completed, saves enrollment and returns to list page
    if request.method == "POST":
        form = EnrollmentForm(request.POST,)
        if form.is_valid():
            form.save()
            return redirect("enrollment_list")
        
    return render(request, "analytics_portal/enrollment/add_enrollment.html", {"form":form})

def update_enrollment(request, id):
    # gets enrollment by id and create the form
    enrollment = Enrollment.objects.get(id = id)
    form = EnrollmentStatusForm(instance=enrollment)

    # if the form has been completed, saves enrollment and returns to list page
    if request.method == "POST":
        form = EnrollmentStatusForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect("enrollment_list")
    
    return render(request, "analytics_portal/enrollment/update_enrollment.html",{"form":form})

# --------------------
# Courses
# --------------------

def course_list(request):
    courses = Course.objects.all()

    return render(request, 'analytics_portal/course/course_list.html', {'courses':courses})

# --------------------
# Sessions 
# --------------------
def session_list(request):
    sessions = Session.objects.all()

    return render(request, 'analytics_portal/session/session_list.html', {'sessions':sessions})

