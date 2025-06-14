from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from authentication.models import CustomUser
from django.views import View
from jobs.forms import JobPostForm
from django.shortcuts import get_object_or_404
from jobs.models import Job

# Create your views here.

@method_decorator(login_required, name='dispatch')
class EmployerDashboardView(View):
    def get(self, request):
        # Optional: ensure this user is an employer
        try:
            if request.user.customuser.role != 'employer':
                return redirect('login_page')
        except CustomUser.DoesNotExist:
            return redirect('login_page')

        return render(request, 'employers/employer_dashboard.html')
    

@method_decorator(login_required, name='dispatch')
class EmployerContactView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'employers/contact.html')
    
    
@method_decorator(login_required, name='dispatch')    
class EmployerAboutView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'employers/about.html')

@method_decorator(login_required, name='dispatch')     
class PostJobView(View):

    def get(self, request):

        form = JobPostForm()

        return render(request, 'employers/post_job.html', {'form': form})

    def post(self, request):

        form = JobPostForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('job_list_page')  # replace with your success URL
        
        print("FORM ERRORS:")

        for field, errors in form.errors.items():

            print(f"{field}: {errors}")

        return render(request, 'jobs/post_job.html', {'form': form})
    

@method_decorator(login_required, name='dispatch') 
class JobListView(View):

    def get(self, request,*args,**kwargs):

        jobs = Job.objects.all()
        data = {'jobs':jobs}

        return render(request,'employers/job_list.html',context=data)
    
@method_decorator(login_required, name='dispatch') 
class JobDetailsView(View):

    def get(request,*args,**kwargs):

        uuid = kwargs.get('uuid')
        job = get_object_or_404(Job, uuid=uuid)
        data = {'job':job}

        return render(request,'employers/job_details.html',context=data)