from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from .models import Cart, CartItem
from django.http import JsonResponse

def get_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        cart, created = Cart.objects.get_or_create(user=None)
    return cart

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_cart(request)
    quantity = int(request.GET.get('quantity', 1))
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    else:
        cart_item.quantity = quantity
        cart_item.save()

    return redirect('cart:cart')


def view_cart(request):
    cart = get_cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)

    if request.method == 'POST':
        quantity_to_remove = int(request.POST.get('quantity'))
        if quantity_to_remove >= cart_item.quantity:
            cart_item.delete()
        else:
            cart_item.quantity -= quantity_to_remove
            cart_item.save()

        return JsonResponse({'status': 'success'})

    return redirect('cart:cart')
