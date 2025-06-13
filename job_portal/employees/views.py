from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from authentication.models import CustomUser

# Create your views here.

@method_decorator(login_required, name='dispatch')
class EmployeeDashboardView(View):

    def get(self, request):

        try:
            if request.user.customuser.role != 'job_seeker':
                return redirect('login_page')
            
        except CustomUser.DoesNotExist:
            return redirect('login_page')
        
        return render(request, 'employees/jobseeker_dashboard.html')
    


@method_decorator(login_required, name='dispatch')
class EmployeeContactView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'employees/contact.html')
    
    
@method_decorator(login_required, name='dispatch')    
class EmployeeAboutView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'employees/about.html')