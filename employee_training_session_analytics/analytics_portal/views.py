from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Enrollment

# Create your views here.
def test(request):
    return render(request, 'analytics_portal/test.html')

def employee_list(request):
    employees = Employee.objects.all()

    return render(request, 'analytics_portal/employee/employee_list.html', {"employees":employees})