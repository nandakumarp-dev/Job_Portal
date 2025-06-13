from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from .forms import UserRegistrationForm, EmployerProfileForm, JobSeekerProfileForm
from .models import CustomUser

# Create your views here.

class LoginView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'authentication/login.html')
    
    def post(self,request,*args,**kwargs):

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
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
        

class LogoutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect('landing_page') 


class UserSelectionView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'authentication/user_selection.html')
         

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

            custom_user = CustomUser.objects.create(user=user, role='job_seeker')

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
