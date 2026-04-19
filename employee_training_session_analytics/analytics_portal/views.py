from django.shortcuts import render, redirect
from datetime import datetime
from .models import Employee, Enrollment, Course, Session
from .forms import EmployeeForm, EnrollmentForm, EnrollmentStatusForm, CourseForm, SessionForm
from django.db.models import Count

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
        department_participation =(
            Enrollment.objects
            .filter(status='2') # filter the Enrollments to only includes status 2 (Completed) 
            .values('employee__department') #group by department
            .annotate(completed_count=Count('id')) #count enrollments
            .order_by('-completed_count') #sorts by highest count 
        )

        # convert to readable format 
        departments = []
        dept_choices = Employee._meta.get_field('department').choices
        dept_dict = dict(dept_choices) #converts the dept choices to dictionary, then you can look it up the names by code, original was a tuple 

        for i in department_participation:
            dept_value = i['employee__department']
            dept_name = dept_dict.get(dept_value, dept_value) #gets the name not the number 
            completed = i['completed_count']
            departments.append({
                'name': dept_name, 
                'completed': completed
            })


        return render(request, "analytics_portal/analytics/analytics.html", {"page": page_filter, 'departments':departments} )
    
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
    # gets the categories for the dropdown menu, displays results if category is chosen 
    category_filter = request.GET.get('category', '')
    categories = Course._meta.get_field('category').choices 

    courses = Course.objects.all()

    # filters categories if one is chosen
    if category_filter:
        courses = courses.filter(category=category_filter)

    return render(request, 'analytics_portal/course/course_list.html', {'courses':courses, "categories":categories})

def add_course(request):
    #creates form
    form = CourseForm()

    #if form is completed, saves course and returns to courses page

    if request.method == "POST":
        form = CourseForm(request.POST, )
        if form.is_valid():
            form.save()
            return redirect('course_list')
        
    return render(request, "analytics_portal/course/add_course.html", {"form":form})

def update_course(request, id):
    #gets course from the id and creates form 
    course = Course.objects.get(id = id)
    form = CourseForm(instance=course)

    # if form has been completed, saves and returns to courses page
    if request.method =="POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    
    return render(request, "analytics_portal/course/update_course.html", {"form":form})

def delete_course(request, id):
    #deletes the course from the id 
    course = Course.objects.get(id=id)
    course.delete()

    return redirect("course_list")


# --------------------
# Sessions 
# --------------------
def session_list(request):
    #starts results with all sessions 
    sessions = Session.objects.all()
    #dictionary to store error messages, didn't need in the end. Good to know for future 
    errors = {}

    #Search parameter from the form 
    search_date_start = request.GET.get('date_start', '')
    search_date_end = request.GET.get('date_end', '')
    search_instructor = request.GET.get('instructor_name', '')

    #filter by Instructor 
    if search_instructor:
        sessions = sessions.filter(instructor_name__icontains=search_instructor)

    #filter by start_date
    if search_date_start:
        try: 
            start_date = datetime.strptime(search_date_start, '%Y-%m-%d').date()
            sessions = sessions.filter(session_date__date__gte=start_date)
        except ValueError: #was not needed in the end but good to know for future developments
            errors['date_start']='Invalid Format, Use:YYYY-MM-DD'
    
    #filter by end_date
    if search_date_end:
        try: 
            end_date = datetime.strptime(search_date_end, '%Y-%m-%d').date()
            sessions = sessions.filter(session_date__date__lte=end_date)
        except ValueError:#was not needed in the end, good to know for future developments 
            errors['date_end']='Invalid Format, Use:YYYY-MM-DD'


    return render(request, 'analytics_portal/session/session_list.html', {'sessions':sessions, 'search_instructor':search_instructor, 'search_date_start':search_date_start, 'search_date_end':search_date_end,'errors':errors,} )


def add_session(request):
    form = SessionForm()

    if request.method =="POST":
        form = SessionForm(request.POST,)
        if form.is_valid():
            form.save()
            return redirect('session_list')
    return render(request, "analytics_portal/session/add_session.html", {'form':form})


def update_session(request, id):
    session = Session.objects.get(id=id)
    form = SessionForm(instance=session)

    if request.method == "POST":
        form = SessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('session_list')

    return render(request, 'analytics_portal/session/update_session.html', {'form':form})

def delete_session(request, id):
    session = Session.objects.get(id=id)
    session.delete()

    return redirect('session_list')
