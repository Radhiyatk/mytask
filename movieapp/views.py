from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.text import slugify

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
        movie_list = Movie.objects.all()
    paginator=Paginator(movie_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        movies=paginator.page(page)
    except (EmptyPage,InvalidPage):
        movies=paginator.page(Paginator.num_pages)

    return render(request,'Category.html',{'category':c_page,'movies':movies})
def MovieDetail(request,c_slug,movie_slug):
    try:
        movie=Movie.objects.get(category__slug=c_slug,slug=movie_slug)
    except Exception as e:
        raise e
    return render(request,'movie.html',{'movie':movie})


def add_movie(request):
    if request.method == "POST":
        cat= request.POST.get('category', )
        print(cat)
        category=Category.objects.get(id=cat)
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        release_date = request.POST.get('release_date',)
        poster = request.FILES['poster']
        actor = request.POST.get('actor',)
        actress = request.POST.get('actress',)
        review = request.POST.get('review',)
        ratings = request.POST.get('ratings',)
        m_link=slugify(name)
        ylink = request.POST.get('ylink',)
        movie = Movie(name=name,slug=m_link,desc=desc,release_date=release_date,poster=poster,actor=actor,
                      actress=actress,review=review,ratings=ratings,ylink=ylink,category=category)
        movie.save()
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
#def detail(request,movie_id):
 #    movies=Movie.objects.get(id=movie_id)
  #   return render(request,'movie.html',{'movie':movies})


