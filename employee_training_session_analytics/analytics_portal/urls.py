from django.urls import path 
from . import views

urlpatterns = [
    path('', views.test),
    path('employees/',views.employee_list,name="employee_list")
]