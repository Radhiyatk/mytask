from django.http import HttpResponse
from django.shortcuts import render, redirect
from movieapp.models import Movie, Category
from .forms import MovieForm
# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,InvalidPage


# Create your views here.
def AllCategory(request,c_slug=None):
    c_page=None
    movie_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        movie_list = Movie.objects.all().filter(category=c_page)
    else:
        movie_list = Movie.objects.all().filter()
    paginator=Paginator(movie_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        movies=paginator.page(page)
    except (EmptyPage,InvalidPage):
        movies=paginator.page(Paginator.num_pages)

    return render(request,'category.html',{'category':c_page,'movies':movies})
def MovieDetail(request,c_slug,movie_slug):
    try:
        movie=Movie.objects.get(category__slug=c_slug,slug=movie_slug)
    except Exception as e:
        raise e
    return render(request,'movie.html',{'movie':movie})




