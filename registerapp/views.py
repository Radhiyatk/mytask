from audioop import reverse

from django.shortcuts import render
from email import message
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.text import slugify


from movieapp.forms import MovieForm
from movieapp.models import Movie,Category


# Create your views here.

def login(request):

    if request.method=='POST':
       username=request.POST['username']
       password=request.POST['password']
       user=auth.authenticate(username=username,password=password)
       if user is not None:
           auth.login(request,user)
           return redirect('/')
       else:
           messages.info(request, "invalid credentials")
           return redirect('login')

    return render(request,'login.html')
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['conpwd']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
               messages.info(request,"Username Taken")
               return redirect("registerapp:register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email taken")
                return redirect("registerapp:register")
            else:
               user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password,
                                    email=email)
               user.save()
               return redirect("registerapp:login")
        else:
            messages.info(request,"password does n't match")
            return redirect("registerapp:register")
        return redirect('/')
    return render(request,'registration.html')
def logout(request):
    auth.logout(request)
    return redirect('/')


