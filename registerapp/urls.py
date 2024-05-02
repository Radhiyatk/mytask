
from django.urls import path
from registerapp import views, admin
app_name="registerapp"

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),


]