from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from product.models import Product

def get_cart(request):
    cart = request.session.get('cart', {})
    return cart


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.GET.get('quantity', 1))

    cart = get_cart(request)

    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += quantity
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': quantity,
            'image_url': product.imag.url if product.imag else ''
        }

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart:cart')


def view_cart(request):
    cart = get_cart(request)
    total_price = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'cart/cart.html', {'cart': cart, 'total_price': total_price})


def remove_from_cart(request, product_id):
    cart = get_cart(request)

    if str(product_id) in cart:
        if request.method == 'POST':
            quantity_to_remove = int(request.POST.get('quantity', 1))
            if cart[str(product_id)]['quantity'] <= quantity_to_remove:
                del cart[str(product_id)]
            else:
                cart[str(product_id)]['quantity'] -= quantity_to_remove

            request.session['cart'] = cart
            request.session.modified = True  # ذخیره تغییرات
            return JsonResponse({'status': 'success'})

    return redirect('cart:cart')


