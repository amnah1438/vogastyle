from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile


# ============================
# 📌 إنشاء حساب جديد
# ============================
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        city = request.POST.get("city")
        country = request.POST.get("country")
        address = request.POST.get("address")

        # تحقق: هل اسم المستخدم مستخدم مسبقًا؟
        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم مستخدم مسبقًا ❌")
            return redirect("accounts:register")

        # إنشاء المستخدم
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # إنشاء ملف المستخدم
        UserProfile.objects.create(
            user=user,
            phone=phone,
            city=city,
            country=country,
            address=address
        )

        # تسجيل الدخول تلقائيًا
        login(request, user)
        messages.success(request, "تم إنشاء حسابك بنجاح ✔️")
        return redirect("/")

    return render(request, "accounts-templates/register.html")



# ============================
# 📌 تسجيل دخول
# ============================
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "تم تسجيل الدخول بنجاح ✔️")
            return redirect("/")
        else:
            messages.error(request, "بيانات تسجيل الدخول غير صحيحة ❌")

    return render(request, "accounts-templates/login.html")



# ============================
# 📌 الملف الشخصي
# ============================
@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, "accounts-templates/profile.html", {"profile": profile})



# ============================
# 📌 تحديث الملف الشخصي
# ============================
@login_required
def update_profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        # تحديث البريد
        request.user.email = request.POST.get("email")
        request.user.save()

        # تحديث البيانات الإضافية
        profile.phone = request.POST.get("phone")
        profile.city = request.POST.get("city")
        profile.country = request.POST.get("country")
        profile.address = request.POST.get("address")
        profile.save()

        messages.success(request, "تم تحديث معلومات حسابك بنجاح ✔️")
        return redirect("accounts:profile")

    return render(request, "accounts-templates/update_profile.html", {
        "profile": profile
    })

