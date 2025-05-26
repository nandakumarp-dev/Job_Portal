from django.shortcuts import render,redirect
from django.views import View

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import UserRegistrationForm, EmployerProfileForm, JobSeekerProfileForm
from .models import CustomUser, EmployerProfile

# Create your views here.

class LoginView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'authentication/login.html')
    
    def post(self,request,*args,**kwargs):

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:

            try:
                custom_user = CustomUser.objects.get(user=user)
                if custom_user.role == 'employer':
                    return redirect('employer_dashboard')
                elif custom_user.role == 'job_seeker':
                    return redirect('jobseeker_dashboard')
            except CustomUser.DoesNotExist:
                pass

            return redirect('home_page')
        
        messages.error(request, "Invalid username or password")
        return render(request, 'authentication/login.html')
        

        

class EmployerRegistrationView(View):

    def get(self,request,*args,**kwargs):

        user_form = UserRegistrationForm()
        profile_form = EmployerProfileForm()

        return render(request,'authentication/register_employer.html', {

            'user_form' : user_form,
            'profile_form' : profile_form
            
        })
    
    def post(self,request,*args,**kwargs):

        user_form = UserRegistrationForm(request.POST)
        profile_form = EmployerProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            
            # Save user
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            
            # Save CustomUser with role
            custom_user = CustomUser.objects.create(user=user, role='employer')
 
            # Save EmployerProfile
            profile = profile_form.save(commit=False)
            profile.custom_user = custom_user
            profile.save()

            messages.success(request,"Employer account created succcessfully! Please login.")
            return redirect('login_page')
        
        messages.error(request, "There was an error in your registration form.")
        return render(request, 'authentication/register_employee.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })
        

class EmployeeRegistrationView(View):

    def get(self,request,*args,**kwargs):

        user_form = UserRegistrationForm()
        profile_form = JobSeekerProfileForm()

        return render(request,'authentication/register_employee.html',{
            'user_form' : user_form,
            'profile_form': profile_form
        })
    
    def post(self,request,*args,**kwargs):

        user_form = UserRegistrationForm(request.POST)
        profile_form = JobSeekerProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            custom_user = CustomUser.objects.create(user=user, role='jobseeker')

            profile = profile_form.save(commit=False)
            profile.custom_user = custom_user
            profile.save()

            messages.success(request, "Job Seeker account created successfully! Please login.")
            return redirect('login_page')
        
        messages.error(request,"There was an error in your registration form.")
        return render(request, 'authentication/register_employee.html', {
            'user_form': user_form,
            'profile_form' : profile_form
        })
    


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render, redirect
from .models import CustomUser

@method_decorator(login_required, name='dispatch')
class EmployerDashboardView(View):
    def get(self, request):
        # Optional: ensure this user is an employer
        try:
            if request.user.customuser.role != 'employer':
                return redirect('login_page')
        except CustomUser.DoesNotExist:
            return redirect('login_page')

        return render(request, 'authentication/employer_dashboard.html')

@method_decorator(login_required, name='dispatch')
class EmployeeDashboardView(View):
    def get(self, request):
        try:
            if request.user.customuser.role != 'job_seeker':
                return redirect('login_page')
        except CustomUser.DoesNotExist:
            return redirect('login_page')

        return render(request, 'authentication/jobseeker_dashboard.html')
