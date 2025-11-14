from django.shortcuts import render, get_object_or_404
from .models import Product, Category


# ============================
#  عرض جميع المنتجات
# ============================
def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'page_title': 'جميع المنتجات'
    }
    return render(request, 'catalog-templates/product_list.html', context)


# ============================
#  عرض المنتجات حسب التصنيف
# ============================
def products_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = category.products.all().order_by('-created_at')

    context = {
        'category': category,
        'products': products,
        'page_title': f'تصنيف: {category.name}'
    }
    return render(request, 'catalog-templates/category_list.html', context)


# ============================
#  صفحة تفاصيل المنتج
# ============================
def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    images = product.images.all()  # الصور الإضافية

    context = {
        'product': product,
        'images': images,
        'page_title': product.name
    }
    return render(request, 'catalog-templates/product_detail.html', context)


# ============================
#  صفحة عروض المنتجات
# ============================
def offers(request):
    products = Product.objects.all().order_by('-created_at')[:20]

    context = {
        'products': products,
        'page_title': 'عروض خاصة'
    }
    return render(request, 'catalog-templates/offers.html', context)
