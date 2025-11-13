from django.db import models
from django.contrib.auth.models import User

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

    class Meta:
        verbose_name = "ملف المستخدم"
        verbose_name_plural = "ملفات المستخدمين"

    def __str__(self):
        return self.user.username
