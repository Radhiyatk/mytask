from django.urls import path
from searchapp import views
app_name='search_app'

urlpatterns = [
    path('',views.SearchQuery,name='SearchQuery'),
]
