from django.urls import path

from EComm.settings import MEDIA_ROOT
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'exp'
urlpatterns = [
    path('', views.FirstView.as_view(), name='first'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('aboutus/', views.AboutUs.as_view(), name='aboutus'),
    path('main/<int:pk>/product_list', views.ProductList.as_view(), name='product_list'),
    path('main/<int:pk>/product_detail', views.ProductDetail.as_view(), name='product_detail'),
    path('test/', views.TestView.as_view(), name='test'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)