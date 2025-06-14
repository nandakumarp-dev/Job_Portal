from django.shortcuts import render,redirect
from django.views import View
from .forms import JobPostForm

# Create your views here.
    
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
    
