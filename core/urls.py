from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),                     # الصفحة الرئيسية
    path('splash/', views.splash, name='splash'),          # شاشة البداية

    # ============================
    #  مسار تغيير الدولة (جديد)
    # ============================
    path('set-country/', views.set_country, name='set_country'),
]
