from django.urls import path
from .import views
app_name='movieapp'
urlpatterns = [
    path('', views.AllCategory, name='AllCategory'),
    path('<slug:c_slug>/', views.AllCategory, name='movie_by_category'),
    path('<slug:c_slug>/<slug:movie_slug>', views.MovieDetail, name='MovieDetail'),



]