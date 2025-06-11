from django.urls import path

from . import views

urlpatterns = [

    path('dashboard/employer/', views.EmployerDashboardView.as_view(), name='employer_dashboard'),
    path('dashboard/employee/', views.EmployeeDashboardView.as_view(), name='jobseeker_dashboard'),
         
]