from django.db import models

class SiteSetting(models.Model):
    site_name = models.CharField(
        max_length=100,
        default="VogaStyle",
        verbose_name="اسم الموقع"
    )
    logo = models.ImageField(
        upload_to='logo/',
        blank=True,
        null=True,
        verbose_name="شعار الموقع"
    )
    footer_text = models.TextField(
        blank=True,
        null=True,
        verbose_name="نص الفوتر"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="تاريخ التحديث"
    )

    class Meta:
        verbose_name = "إعداد الموقع"
        verbose_name_plural = "إعدادات الموقع"

    def __str__(self):
        return self.site_name
