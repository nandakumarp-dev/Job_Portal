from django.urls import path
from . import views

urlpatterns = [
    
    path('post_job/', views.PostJobView.as_view(), name='post_job_page'),

]