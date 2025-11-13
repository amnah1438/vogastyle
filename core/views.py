from django.shortcuts import render

def home(request):
    # عرض الصفحة الرئيسية من داخل مجلد core-templates
    return render(request, "home.html")
