from django.shortcuts import render, redirect
from catalog.models import Product   # <-- مهم جداً


# ============================
# شاشة البداية Splash Screen
# ============================
def splash(request):
    return render(request, "core-templates/splash.html")


# ============================
# الصفحة الرئيسية Home
# ============================
def home(request):
    # جلب آخر المنتجات
    products = Product.objects.all().order_by('-created_at')[:12]

    context = {
        "products": products,
    }

    return render(request, "core-templates/home.html", context)


# ============================
# تغيير الدولة (Country Switch)
# ============================
def set_country(request):
    if request.method == "POST":
        country = request.POST.get("country")
        request.session["country"] = country   # نحفظها في الجلسة Session

    # نرجّع المستخدم لنفس الصفحة التي كان عليها
    return redirect(request.META.get("HTTP_REFERER", "/"))
