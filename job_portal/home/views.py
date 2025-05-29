from django.shortcuts import render,redirect

from django.views import View

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from authentication.models import CustomUser

# Create your views here.

class HomeView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'home/home.html')

class AboutView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'home/about.html')
    
class ContactView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'home/contact.html')
    
class FindJobView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'home/find_a_job.html')
    
class PostJobView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'home/post_a_job.html')
    

class UserSelectionView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'authentication/user_selection.html')
    

@method_decorator(login_required, name='dispatch')
class EmployerDashboardView(View):
    def get(self, request):
        # Optional: ensure this user is an employer
        try:
            if request.user.customuser.role != 'employer':
                return redirect('login_page')
        except CustomUser.DoesNotExist:
            return redirect('login_page')

        return render(request, 'home/employer_dashboard.html')

@method_decorator(login_required, name='dispatch')
class EmployeeDashboardView(View):
    def get(self, request):
        try:
            if request.user.customuser.role != 'job_seeker':
                return redirect('login_page')
        except CustomUser.DoesNotExist:
            return redirect('login_page')

        return render(request, 'home/jobseeker_dashboard.html')
    

class FindJobView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'home/findjob.html')