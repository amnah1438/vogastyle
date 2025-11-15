from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('splash/', views.splash, name='splash'),
    path('set-country/', views.set_country, name='set_country'),

    # الأقسام
    path('women/', views.women, name='women'),
    path('men/', views.men, name='men'),
    path('kids/', views.kids, name='kids'),
    path('beauty/', views.beauty, name='beauty'),
    path('home-category/', views.home_category, name='home_category'),
]
