from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),       # الصفحة الرئيسية
    path('splash/', views.splash, name='splash'),   # شاشة البداية
]
