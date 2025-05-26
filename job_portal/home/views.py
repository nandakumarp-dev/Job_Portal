from django.shortcuts import render

from django.views import View

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
    
class TestView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'home/test.html')
    

class UserSelectionView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'authentication/user_selection.html')

