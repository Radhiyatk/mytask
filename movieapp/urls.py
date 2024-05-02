from django.urls import path
from .import views
app_name='movieapp'
urlpatterns = [

    path('<slug:c_slug>/', views.AllCategory, name='movie_by_category'),
    path('<slug:c_slug>/<slug:movie_slug>', views.MovieDetail, name='MovieDetail'),
    path('add_movie', views.add_movie, name='add_movie'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('', views.AllCategory, name='AllCategory'),

]