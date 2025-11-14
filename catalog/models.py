from django.db import models
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="اسم التصنيف"
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="الرابط (Slug)"
    )
    image = CloudinaryField(
        folder="categories/",
        blank=True,
        null=True,
        verbose_name="صورة التصنيف"
    )

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="التصنيف"
    )
    name = models.CharField(
        max_length=200,
        verbose_name="اسم المنتج"
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="الرابط (Slug)"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="الوصف"
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="السعر"
    )
    stock = models.PositiveIntegerField(
        default=0,
        verbose_name="المخزون"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإضافة"
    )

    # الصورة الرئيسية للمنتج من Cloudinary
    main_image = CloudinaryField(
        folder="products/",
        verbose_name="الصورة الرئيسية"
    )

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="المنتج"
    )

    # الصور الإضافية للمنتج من Cloudinary
    image = CloudinaryField(
        folder="products/extra/",
        verbose_name="الصورة"
    )

    class Meta:
        verbose_name = "صورة إضافية"
        verbose_name_plural = "صور إضافية"

    def __str__(self):
        return f"صورة - {self.product.name}"
