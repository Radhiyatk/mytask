from audioop import reverse

from django.shortcuts import render
from email import message
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from movieapp.forms import MovieForm
from movieapp.models import Movie,Category


# Create your views here.





# Create your views here.
def add_movie(request):
    if request.method == "POST":
        title = request.POST.get('title',)
        desc = request.POST.get('desc',)
        release_date = request.POST.get('release_date',)
        poster = request.FILES['poster']
        actor = request.POST.get('actor',)
        actress = request.POST.get('actress',)
        ylink = request.POST.get('ylink',)
        movie = Movie(title=title,desc=desc,release_date=release_date,poster=poster,actor=actor,actress=actress,ylink=ylink)
        movie.save();
        return redirect('/')
    return  render(request, 'add_movie.html')
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return  render(request,'update.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method == 'POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return  render(request,"delete.html")
def detail(request,movie_id):
    movies=Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':movies})



def login(request):

    if request.method=='POST':
       username=request.POST['username']
       password=request.POST['password']
       user=auth.authenticate(username=username,password=password)
       if user is not None:
           auth.login(request,user)
           return render(request,'navbar2.html')
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
               return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email taken")
                return redirect('register')
            else:
               user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password,
                                    email=email)
               user.save()
               return redirect('login')
        else:
            messages.info(request,"password does n't match")
            return redirect('register')
        return redirect('/')
    return render(request,'registration.html')
def logout(request):
    auth.logout(request)
    return redirect('/')


