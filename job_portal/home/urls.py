from django.urls import path

from . import views

urlpatterns = [

    path('home/',views.HomeView.as_view(),name='home_page'),
    path('about/',views.AboutView.as_view(),name='about_page'),
    path('contact/',views.ContactView.as_view(),name='contact_page'),
    path('postjob/',views.PostJobView.as_view(),name='post_job_page'),
    path('userselection/',views.UserSelectionView.as_view(),name='user_selection_page'),
    path('dashboard/employer/', views.EmployerDashboardView.as_view(), name='employer_dashboard'),
    path('dashboard/employee/', views.EmployeeDashboardView.as_view(), name='jobseeker_dashboard'),
    path('findjob/',views.FindJobView.as_view(),name='find_job_page'),    
    
]