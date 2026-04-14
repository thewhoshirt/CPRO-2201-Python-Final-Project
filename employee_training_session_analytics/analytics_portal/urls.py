from django.urls import path 
from . import views

urlpatterns = [
    path('', views.test),
    path('employees/',views.employee_list,name="employee_list"),
    path('employees/add/', views.add_employee, name="add_employee"),
    path('employees/update/<int:id>/', views.update_employee, name="update_employee"),
    path('employees/delete/<int:id>/', views.delete_employee, name="delete_employee"),
    path('enrollments/',views.enrollment_list,name="enrollment_list"),
    path('enrollments/add/', views.add_enrollment, name="add_enrollment"),
    path('enrollments/update/<int:id>/', views.update_enrollment, name="update_enrollment"),
    path('enrollments/<int:id>',views.employee_enrollment_list,name="employee_enrollment_list"),
    path('enrollments/<int:id>/update',views.update_status,name="update_status"),
    path('courses/',views.course_list,name="course_list" ), 
]