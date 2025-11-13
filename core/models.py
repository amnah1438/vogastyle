from django.db import models

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, default="VogaStyle")
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    footer_text = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "إعداد الموقع"
        verbose_name_plural = "إعدادات الموقع"

    def __str__(self):
        return self.site_name
