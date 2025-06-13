from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from authentication.models import CustomUser
from django.views import View

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