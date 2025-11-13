from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # لوحة التحكم
    path('admin/', admin.site.urls),

    # ============================
    # مسارات التطبيقات
    # ============================
    path('', include('core.urls')),            # الصفحة الرئيسية والتخطيط العام
    path('accounts/', include('accounts.urls')),
    path('catalog/', include('catalog.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('payments/', include('payments.urls')),
    path('marketing/', include('marketing.urls')),
]
