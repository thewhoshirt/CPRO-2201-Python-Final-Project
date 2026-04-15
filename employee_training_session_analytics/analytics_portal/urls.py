from django.urls import path 
from . import views

urlpatterns = [
    path('', views.test),
    # analytics
    path('analytics/',views.analytics,name="analytics"),
    # employees
    path('employees/',views.employee_list,name="employee_list"),
    path('employees/add/', views.add_employee, name="add_employee"),
    path('employees/update/<int:id>/', views.update_employee, name="update_employee"),
    path('employees/delete/<int:id>/', views.delete_employee, name="delete_employee"),
    # enrollments
    path('enrollments/',views.enrollment_list,name="enrollment_list"),
    path('enrollments/add/', views.add_enrollment, name="add_enrollment"),
    path('enrollments/update/<int:id>/', views.update_enrollment, name="update_enrollment"),
    # courses
    path('courses/',views.course_list,name="course_list" ), 
]