from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from movieapp.models import Movie
from django.db.models import Q
# Create your views here.
def SearchQuery(request):
    movies=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        movies=Movie.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return  render(request,'search.html',{'query':query,'movies':movies})