from django.shortcuts import render,redirect
from django.views import View

from django.contrib.auth import authenticate, login

from django.contrib import messages

from django.contrib.auth.models import User

# Create your views here.

class LoginView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'authentication/login.html')
    
    def post(self,request,*args,**kwargs):

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:

            login(request, user)

            return redirect('home_page')
        
        else:
            messages.error(request,"Invalid username or password")
            
            return render(request, 'authentication/login.html')
        


class RegisterUserView(View):

    def get(self,request,*args,**kwargs):

        return render(request,'authentication/register_user.html')
    
    def post(self,request,*args,**kwargs):

        username = request.POST.get('username')

        email = request.POST.get('email')

        password = request.POST.get('password')

        # password2 = request.POST.get('password2')

        if not username or not email or not password:

            messages.error(request,"Please fill out all fields.")

            return render(request,'authentication/register_user.html')
        
        if User.objects.filter(email=email).exists():

            messages.error(request,"This email is already registered with another account")

            return render(request,'authentication/register_user.html')
        
        user = User.objects.create_user(username=username,email=email,password=password)

        user.save()

        messages.success(request,"Account created successfully! Please login.")

        return redirect('login_page')
    

