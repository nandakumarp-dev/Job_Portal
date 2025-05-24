from django.urls import path

from . import views

urlpatterns = [

    path('home/',views.HomeView.as_view(),name='home_page'),
    path('about/',views.AboutView.as_view(),name='about_page'),
    path('contact/',views.ContactView.as_view(),name='contact_page'),
    path('findjob',views.FindJobView.as_view(),name='find_job_page'),
    path('PostJob',views.PostJobView.as_view(),name='post_job_page'),
    
]