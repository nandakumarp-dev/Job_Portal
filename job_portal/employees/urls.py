from django.urls import path
from . import views

urlpatterns = [

    path('dashboard/employee/', views.EmployeeDashboardView.as_view(), name='employee_dashboard'),
    path('employee_dashboard/contact/',views.EmployeeContactView.as_view(),name='employees_contact_page'),
    path('employee_dashboard/about/',views.EmployeeAboutView.as_view(),name='employees_about_page'),
    path('employee_dashboard/apply_job/',views.ApplyJobView.as_view(),name='apply_job_page'),
    path('employee_dashboard/job_details/<str:uuid>', views.JobDetailsView.as_view(), name='job_details_page'),
    path('employee_dashboard/jobs_list', views.JobListView.as_view(), name='jobs_list_page'),
         
]