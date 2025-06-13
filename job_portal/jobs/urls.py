from django.urls import path
from . import views

urlpatterns = [
    
    path('job_details/<str:uuid>', views.JobDetailsView.as_view(), name='job_details_page'),
    path('post_job/', views.PostJobView.as_view(), name='post_job_page'),
    path('job_list/', views.JobListView.as_view(), name='job_list_page'),
    path('findjob/',views.FindJobView.as_view(),name='find_job_page'),

]