from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('detaile_view/', include('product.urls', namespace='product_ditail')),
    path('about_us/', include('about.urls', namespace='about')),
    path('login/', include('account.urls', namespace='account')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
