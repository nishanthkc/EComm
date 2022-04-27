from django.urls import path
from . import views

app_name = 'exp'
urlpatterns = [
    path('', views.FirstView.as_view(), name='first'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),

]