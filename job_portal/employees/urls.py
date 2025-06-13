from django.urls import path
from . import views

urlpatterns = [

    path('dashboard/employee/', views.EmployeeDashboardView.as_view(), name='jobseeker_dashboard'),
    path('employee_dashboard/contact/',views.EmployeeContactView.as_view(),name='employees_contact_page'),
    path('employee_dashboard/about/',views.EmployeeAboutView.as_view(),name='employees_about_page'),
         
]