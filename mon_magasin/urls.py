from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية = products
    path('', include('products.urls')),

    # cart
    path('cart/', include('cart.urls')),

    # orders
    path('orders/', include('orders.urls')),
]

# نخلي media يخدم حتى في DEBUG=False
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)