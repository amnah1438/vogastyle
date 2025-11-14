from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns   # <-- مهم جداً للتعدد اللغوي

# لدعم ملفات MEDIA في التطوير
from django.conf import settings
from django.conf.urls.static import static


# ================================
# مسار تغيير اللغة
# ================================
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),   # <-- هذا يُفَعّل التبديل بين اللغات
]


# ================================
# المسارات العامة داخل i18n
# ================================
urlpatterns += i18n_patterns(

    # لوحة التحكم
    path('admin/', admin.site.urls),

    # التطبيقات
    path('', include('core.urls')),        # الصفحة الرئيسية
    path('accounts/', include('accounts.urls')),
    path('catalog/', include('catalog.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('payments/', include('payments.urls')),
    path('marketing/', include('marketing.urls')),

)


# ================================
# دعم MEDIA في التطوير
# ================================
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
