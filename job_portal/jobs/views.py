from django.shortcuts import render,redirect
from django.views import View
from .forms import JobPostForm
from django.shortcuts import get_object_or_404
from .models import Job

# Create your views here.

class FindJobView(View):

    def get(request,*args,**kwargs):

        jobs = Job.objects.all()
        data = {'jobs':jobs}

        return render(request,'jobs/job_list.html',context=data)
    
class JobDetailsView(View):

    def get(request,*args,**kwargs):

        uuid = kwargs.get('uuid')
        job = get_object_or_404(Job, uuid=uuid)
        data = {'job':job}

        return render(request,'jobs/job_details.html',context=data)
    
class PostJobView(View):

    def get(self, request):

        form = JobPostForm()

        return render(request, 'jobs/post_job.html', {'form': form})

    def post(self, request):

        form = JobPostForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('job_list_page')  # replace with your success URL
        
        print("FORM ERRORS:")

        for field, errors in form.errors.items():

            print(f"{field}: {errors}")

        return render(request, 'jobs/post_job.html', {'form': form})

class JobListView(View):

    def get(self, request,*args,**kwargs):

        jobs = Job.objects.all()

        data = {'jobs':jobs}

        return render(request,'jobs/job_list.html',context=data)