from django.urls import path
from . import views

urlpatterns = [

    path('employer_dashboard/employer/', views.EmployerDashboardView.as_view(), name='employer_dashboard'),
    path('employer_dashboard/contact/',views.EmployerContactView.as_view(),name='employers_contact_page'),
    path('employer_dashboard/about/',views.EmployerAboutView.as_view(),name='employers_about_page'),
    path('employer_dashboard/post_job/', views.PostJobView.as_view(), name='post_job_page'),
    path('employer_dashboard/jobs_list', views.JobListView.as_view(), name='jobs_list_page'),
    path('employer_dashboard/job_details/<str:uuid>', views.JobDetailsView.as_view(), name='job_details_page'),
         
]