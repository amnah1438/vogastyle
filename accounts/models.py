from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="المستخدم"
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="رقم الجوال"
    )

    address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="العنوان"
    )

    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="المدينة"
    )

    country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="الدولة"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإنشاء"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخر تحديث"
    )

    class Meta:
        verbose_name = "ملف المستخدم"
        verbose_name_plural = "ملفات المستخدمين"

    def __str__(self):
        return f"الملف الشخصي لـ {self.user.username}"


# =====================================================
# 📌 إنشاء UserProfile تلقائيًا عند إنشاء المستخدم
# =====================================================
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
