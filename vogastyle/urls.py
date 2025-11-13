from django.contrib import admin
from django.urls import path, include

# لدعم مسارات media أثناء التطوير
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ============================
    # لوحة التحكم
    # ============================
    path('admin/', admin.site.urls),

    # ============================
    # مسارات التطبيقات
    # ============================
    path('', include('core.urls')),                # الصفحة الرئيسية
    path('accounts/', include('accounts.urls')),
    path('catalog/', include('catalog.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('payments/', include('payments.urls')),
    path('marketing/', include('marketing.urls')),
]

# ============================
# دعم ملفات media أثناء التطوير
# ============================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
