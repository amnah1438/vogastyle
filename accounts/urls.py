from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    # تسجيل حساب جديد
    path("register/", views.register_view, name="register"),

    # تسجيل الدخول
    path("login/", views.login_view, name="login"),

    # تسجيل الخروج
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),

    # الملف الشخصي
    path("profile/", views.profile_view, name="profile"),

    # تعديل الملف الشخصي
    path("profile/update/", views.update_profile_view, name="update_profile"),
]
