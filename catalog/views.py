from django.shortcuts import render
from .models import Product, Category


def offers(request):
    """
    صفحة عروض المنتجات – مثال على صفحة جديدة داخل catalog
    """
    products = Product.objects.all().order_by('-created_at')[:20]  # مثال: آخر 20 منتج

    context = {
        'products': products,
        'page_title': 'عروض خاصة'
    }
    return render(request, 'catalog-templates/offers.html', context)
