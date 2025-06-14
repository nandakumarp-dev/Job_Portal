from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from authentication.models import CustomUser
from jobs.models import Job
from django.shortcuts import get_object_or_404

# Create your views here.

@method_decorator(login_required, name='dispatch')
class EmployeeDashboardView(View):

    def get(self, request):

        try:
            if request.user.customuser.role != 'job_seeker':
                return redirect('login_page')
            
        except CustomUser.DoesNotExist:
            return redirect('login_page')
        
        return render(request, 'employees/employee_dashboard.html')


@method_decorator(login_required, name='dispatch')
class EmployeeContactView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'employees/contact.html')
    
    
@method_decorator(login_required, name='dispatch')    
class EmployeeAboutView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'employees/about.html')


@method_decorator(login_required, name='dispatch') 
class ApplyJobView(View):

    def get(request,*args,**kwargs):

        return render(request,'employees/apply_job.html')
    
@method_decorator(login_required, name='dispatch')    
class JobListView(View):

    def get(self, request,*args,**kwargs):

        jobs = Job.objects.all()
        data = {'jobs':jobs}

        return render(request,'employees/job_list.html',context=data)
    
@method_decorator(login_required, name='dispatch') 
class JobDetailsView(View):

    def get(request,*args,**kwargs):

        uuid = kwargs.get('uuid')
        job = get_object_or_404(Job, uuid=uuid)
        data = {'job':job}

        return render(request,'employees/job_details.html',context=data)