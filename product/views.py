from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product/product_details.html', {'product': product})


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'product/category_detail.html', {
        'category': category,
        'products': products,
    })