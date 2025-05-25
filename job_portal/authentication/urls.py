from django.urls import path

from . import views

urlpatterns = [

    path('login/',views.LoginView.as_view(),name='login_page'),

    path('employer_registeration/',views.EmployerRegistrationView.as_view(),name='employer_registration_page'),

    path('employee_registeration/',views.EmployeeRegistrationView.as_view(),name='employee_registration_page'),
]