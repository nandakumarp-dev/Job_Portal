from django.shortcuts import render,redirect
from django.views import View
from .forms import JobPostForm

# Create your views here.


class FindJobView(View):

    def get(request,*args,**kwargs):

        return render()
    
class JobDetailsView(View):

    def get(request,*args,**kwargs):

        return render(request,'jobs/job_details.html')
    

class JobListView(View):

    def get(request,*args,**kwargs):

        return render(request,'jobs/job_list.html')
    

class PostJobView(View):
    def get(self, request):
        form = JobPostForm()
        return render(request, 'jobs/post_job.html', {'form': form})

    def post(self, request):
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')  # replace with your success URL
        
        print("FORM ERRORS:")
        for field, errors in form.errors.items():
            print(f"{field}: {errors}")
        return render(request, 'jobs/post_job.html', {'form': form})


class JobListView(View):

    def get(self, request,*args,**kwargs):

        return render(request,'jobs/job_list.html')