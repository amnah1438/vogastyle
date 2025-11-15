from django.shortcuts import render, redirect
from catalog.models import Product

def splash(request):
    return render(request, "core-templates/splash.html")

def home(request):
    products = Product.objects.all().order_by('-created_at')[:12]

    countries = {
        "sa": "السعودية",
        "ae": "الإمارات",
        "kw": "الكويت",
        "qa": "قطر",
        "bh": "البحرين",
    }

    return render(request, "core-templates/home.html", {
        "products": products,
        "countries": countries,
    })


def set_country(request):
    if request.method == "POST":
        request.session["country"] = request.POST.get("country")
    return redirect(request.META.get("HTTP_REFERER", "/"))

# صفحات الأقسام
def women(request): return render(request, "core-templates/coming.html")
def men(request): return render(request, "core-templates/coming.html")
def kids(request): return render(request, "core-templates/coming.html")
def beauty(request): return render(request, "core-templates/coming.html")
def home_category(request): return render(request, "core-templates/coming.html")
