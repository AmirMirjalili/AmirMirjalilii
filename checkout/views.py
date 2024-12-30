from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import CheckoutForm
from .models import City

def checkout_view(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # ذخیره اطلاعات فرم در مدل Checkout
            form.save()
            # بعد از ذخیره به صفحه موفقیت هدایت می‌شود
            return redirect('checkout_success')
    else:
        form = CheckoutForm()

    return render(request, 'checkout/checkout.html', {'form': form})

def load_cities(request):
    province_id = request.GET.get('province_id')
    if province_id:  # بررسی اگر province_id موجود است
        cities = City.objects.filter(province_id=province_id).values('id', 'name')
        return JsonResponse(list(cities), safe=False)
    else:
        return JsonResponse([], safe=False)  # در صورت نبود province_id داده‌ای ارسال نمی‌شود


def checkout_success(request):
    return render(request, 'checkout/checkout_success.html')
