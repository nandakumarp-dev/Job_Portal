from django.shortcuts import render
from django.views import View

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
    

