from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    # ============================
    # قائمة المنتجات
    # ============================
    path('', views.product_list, name='product_list'),

    # ============================
    # المنتجات حسب التصنيف
    # ============================
    path('category/<slug:category_slug>/', views.products_by_category, name='products_by_category'),

    # ============================
    # صفحة تفاصيل المنتج
    # ============================
    path('<slug:product_slug>/', views.product_detail, name='product_detail'),
]
