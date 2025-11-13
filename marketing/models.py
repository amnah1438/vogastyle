from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to="banners/")
    button_text = models.CharField(max_length=50, blank=True, null=True)
    button_link = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "بانر"
        verbose_name_plural = "البانرات"

    def __str__(self):
        return self.title


class FeaturedCollection(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='collections/')
    link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "كولكشن مميز"
        verbose_name_plural = "كولكشنز مميزة"

    def __str__(self):
        return self.title
