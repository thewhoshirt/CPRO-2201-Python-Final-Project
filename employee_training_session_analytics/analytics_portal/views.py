from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee, Enrollment
from .forms import EmployeeForm

# Create your views here.
def test(request):
    return render(request, "analytics_portal/test.html")

def employee_list(request):
    employees = Employee.objects.all()

    return render(request, "analytics_portal/employee/employee_list.html", {"employees":employees})

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