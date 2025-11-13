from django.db import models

class Banner(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="عنوان البانر"
    )
    subtitle = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name="العنوان الفرعي"
    )
    image = models.ImageField(
        upload_to="banners/",
        verbose_name="صورة البانر"
    )
    button_text = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="نص الزر"
    )
    button_link = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="رابط الزر"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="نشط؟"
    )

    class Meta:
        verbose_name = "بانر"
        verbose_name_plural = "البانرات"

    def __str__(self):
        return self.title


class FeaturedCollection(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="عنوان الكولكشن"
    )
    image = models.ImageField(
        upload_to='collections/',
        verbose_name="صورة الكولكشن"
    )
    link = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="الرابط"
    )

    class Meta:
        verbose_name = "كولكشن مميز"
        verbose_name_plural = "كولكشنز مميزة"

    def __str__(self):
        return self.title
