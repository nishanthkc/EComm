from unicodedata import category
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Category, Product

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

class AboutUs(View):
    def get(self, request):
        return render(request, 'exp/aboutus.html')

class ProductPage(View):
    def get(self, request, pk):
        products = Product.objects.filter(category=pk)
        ctx = {'products':products}
        return render(request, 'exp/productpage.html', ctx)