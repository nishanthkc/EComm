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
    path('main/<int:pk>/product_list', views.ProductList.as_view(), name='product_list'),
    path('main/<int:pk>/product_detail', views.ProductDetail.as_view(), name='product_detail'),
    path('test/', views.TestView.as_view(), name='test'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('wishlist/', views.WishlistView.as_view(), name='wishlist'),

    path('main/add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('cart/remove_from_cart', views.remove_from_cart, name='remove_from_cart'),
    path('cart/move_to_wishlist_from_cart', views.move_to_wishlist_from_cart, name='move_to_wishlist_from_cart'),
    path('main/move_to_wishlist', views.move_to_wishlist, name='move_to_wishlist'),
    path('wishlist/remove_from_wishlist', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/move_to_cart_from_wishlist', views.move_to_cart_from_wishlist, name='move_to_cart_from_wishlist'),


    path('testing/', views.Testing.as_view(), name='testing'),
    path('jsonfun/', views.jsonfun, name='jsonfun'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)