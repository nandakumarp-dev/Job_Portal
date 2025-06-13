from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.LoginView.as_view(), name='login_page'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('user_selection/',views.UserSelectionView.as_view(),name='user_selection_page'),
    path('employer_registration/', views.EmployerRegistrationView.as_view(), name='employer_registration_page'),
    path('employee_registration/', views.EmployeeRegistrationView.as_view(), name='employee_registration_page'),

]
