from django.shortcuts import render
from catalog.models import Product   # <-- مهم جداً

def home(request):
    # جلب آخر المنتجات
    products = Product.objects.all().order_by('-created_at')[:12]

    context = {
        "products": products,
    }

    return render(request, "core-templates/home.html", context)
