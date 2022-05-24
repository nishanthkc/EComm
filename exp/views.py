from unicodedata import category
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Category, Product, Cart, Wishlist
from django.http import JsonResponse
import time

# Create your views here.
class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'exp/index.html')
    def post(self, request):
        return render()

class FirstView(View):
    def get(self, request):
        catg = Category.objects.all()
        prod = Product.objects.all()
        ctx = {'catg':catg, 'prod':prod}
        return render(request, 'exp/first.html', ctx)
    def post(self, request):
        return render()

class SignUp(View):
    def get(self, request):
        return render(request, 'exp/signup.html')
    def post(self, request):
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        #messages.success(request, 'your acc has been successfully created.')
        #myuser.is_active=False
        return redirect(reverse_lazy('exp:first'))


class ProductList(View):
    def get(self, request, pk):
        products = Product.objects.filter(category=pk)
        ctx = {'products':products}
        return render(request, 'exp/product_list.html', ctx)


class ProductDetail(View):
    def get(self, request, pk):
        #products = Product.objects.filter(category=pk)
        my_product = Product.objects.get(pk=pk)
        ctx = {'my_product':my_product}
        return render(request, 'exp/product_detail.html', ctx)


class TestView(View):
    def get(self, request):
        catg = Category.objects.all()
        prod = Product.objects.all()
        trending = Product.objects.filter(product_trending = 1)
        ctx = {'catg':catg, 'prod':prod, 'trending':trending}
        return render(request, 'exp/home.html', ctx)


class CartView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart.objects.filter(user=request.user)
        ctx = {'cart':cart}
        return render(request, 'exp/cart.html', ctx)

class WishlistView(LoginRequiredMixin, View):
    def get(self, request):
        wishlist = Wishlist.objects.filter(user=request.user)
        ctx = {'wishlist':wishlist}
        return render(request, 'exp/wishlist.html', ctx)






def add_to_cart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('prod_id'))
            quantity = int(request.POST.get('product_qty'))

            product_check = Product.objects.get(pk=prod_id)
            if product_check:
                if Cart.objects.filter(user=request.user, product=product_check):
                    return JsonResponse({'status':'Already in cart'})
                else:
                    if product_check.quantity>quantity:
                        Cart.objects.create(user=request.user, product=product_check, product_qty=quantity)
                        return JsonResponse({'status':'Added to cart'})
                    else:    
                        return JsonResponse({'status':'Only '+str(product_check.quantity)+' units available'})
            
            else:
                return JsonResponse({'status':'no such product found'})    


        else:
            return JsonResponse({'status':'Login to continue'})
    return redirect('/')

def remove_from_cart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('prod_id'))
        product_check = Product.objects.get(pk=prod_id)
        if product_check:
            if Cart.objects.filter(user=request.user, product=product_check):
                Cart.objects.filter(user=request.user, product=product_check).delete()
                return JsonResponse({'status':'Product removed from the cart'})
            else:
                return JsonResponse({'status':'Product not in the cart'})
        else:    
            return JsonResponse({'status':'No such product'})
    
    return redirect('/')


def move_to_wishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('prod_id'))
            quantity = int(request.POST.get('product_qty'))

            product_check = Product.objects.get(pk=prod_id)
            if product_check:
                if Wishlist.objects.filter(user=request.user, product=product_check):
                    return JsonResponse({'status':'Already in wishlist'})
                else:
                    if product_check.quantity>quantity:
                        Wishlist.objects.create(user=request.user, product=product_check, product_qty=quantity)
                        return JsonResponse({'status':'Added to wishlist'})
                    else:    
                        return JsonResponse({'status':'Only '+str(product_check.quantity)+' units available'})
            else:
                return JsonResponse({'status':'no such product found'})    
        else:
            return JsonResponse({'status':'Login to continue'})
    return redirect('/')
        

def remove_from_wishlist(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('prod_id'))
        product_check = Product.objects.get(pk=prod_id)
        if product_check:
            if Wishlist.objects.filter(user=request.user, product=product_check):
                Wishlist.objects.filter(user=request.user, product=product_check).delete()
                return JsonResponse({'status':'Product removed from the Wishlist'})
            else:
                return JsonResponse({'status':'Product not in the Wishlist'})
        else:    
            return JsonResponse({'status':'No such product'})
    return redirect('/')


def move_to_cart_from_wishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('prod_id'))
            my_product = Product.objects.get(pk=prod_id)
            wishlist_check = Wishlist.objects.get(product=my_product)
            if wishlist_check:
                if Wishlist.objects.filter(user=request.user, product=my_product):
                    Cart.objects.create(user=request.user, product=my_product, product_qty=wishlist_check.product_qty)
                    Wishlist.objects.get(user=request.user, product=my_product).delete()
                    return JsonResponse({'status':'moved from wishlist to cart'})                
            else:
                return JsonResponse({'status':'no such product found'})    
        else:
            return JsonResponse({'status':'Login to continue'})
    return redirect('/')


def move_to_wishlist_from_cart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('prod_id'))
            my_product = Product.objects.get(pk=prod_id)
            cart_check = Cart.objects.get(product=my_product)
            if cart_check:
                if Cart.objects.filter(user=request.user, product=my_product):
                    Wishlist.objects.create(user=request.user, product=my_product, product_qty=cart_check.product_qty)
                    Cart.objects.get(user=request.user, product=my_product).delete()
                    return JsonResponse({'status':'moved from wishlist to cart'})                
            else:
                return JsonResponse({'status':'no such product found'})    
        else:
            return JsonResponse({'status':'Login to continue'})
    return redirect('/')






class Testing(View):
    def get(self, request):
        return render(request, 'exp/testing.html')

def jsonfun(request):
    time.sleep(2)
    a = []
    for i in range(100):
        a.append(i)
    stuff = {
        'first':'first thing',
        'second':'second thing',
        'a':a
    }
    return JsonResponse(stuff)
        