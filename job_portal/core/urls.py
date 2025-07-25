from django.urls import path
from . import views

urlpatterns = [

    path('',views.LandingView.as_view(),name='landing_page'),
    path('contact/',views.ContactView.as_view(),name='contact_page'),
    path('about/',views.AboutView.as_view(),name='about_page'),
    path('jobs/',views.JobsView.as_view(),name='job_list_page'),
    path('job/<str:uuid>', views.JobDetailsView.as_view(), name='job_detail_page'),

]