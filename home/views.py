from django.shortcuts import render
from django.views import View
from product.models import Product

class HomeView(View):
    def get(self,request):
        product = Product.objects.all()
        return render(request, 'home/home.html', {'product':product})

class special_view(View):
    def get(self,request):
        product_s = Product.objects.all().filter(is_discount=True)
        return render(request, 'home/special.html', {'product_s':product_s})