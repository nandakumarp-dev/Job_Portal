from django.urls import path
from . import views

urlpatterns = [

    path('employer_dashboard/employer/', views.EmployerDashboardView.as_view(), name='employer_dashboard'),
    path('employer_dashboard/contact/',views.EmployerContactView.as_view(),name='employers_contact_page'),
    path('employer_dashboard/about/',views.EmployerAboutView.as_view(),name='employers_about_page'),
         
]