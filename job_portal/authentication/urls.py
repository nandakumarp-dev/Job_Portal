from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('employer_registration/', views.EmployerRegistrationView.as_view(), name='employer_registration_page'),
    path('employee_registration/', views.EmployeeRegistrationView.as_view(), name='employee_registration_page'),

]
