from django.shortcuts import render
from django.views import View
from jobs.models import Job
from django.shortcuts import get_object_or_404

# Create your views here.

class LandingView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'core/landing_page.html')
    
class ContactView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'core/contact_page.html')
    
class AboutView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'core/about_page.html')
    
class JobsView(View):

    def get(self,request,*args,**kwargs):

        jobs = Job.objects.all()
        data = {'jobs':jobs}

        return render(request,'core/jobs_list.html',context=data)
     
class JobDetailsView(View):

    def get(request,*args,**kwargs):

        uuid = kwargs.get('uuid')
        job = get_object_or_404(Job, uuid=uuid)
        data = {'job':job}

        return render(request,'core/job_detail.html',context=data)
