from django.urls import path 
from . import views

urlpatterns = [
    path('home/',views.home, name="home"),
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
    path('courses/add/',views.add_course,name="add_course" ), 
    path('courses/update/<int:id>/',views.update_course,name="update_course" ), 
    path('courses/delete/<int:id>/',views.delete_course,name="delete_course" ), 
    #session
    path('sessions/',views.session_list,name="session_list" ), 
    path('sessions/add/',views.add_session,name="add_session" ), 
    path('sessions/update/<int:id>/',views.update_session, name='update_session' ), 
    path('sessions/delete/<int:id>/',views.delete_session, name="delete_session" ), 
]