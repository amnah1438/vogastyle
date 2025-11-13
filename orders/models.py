from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product

class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="الزبون"
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="إجمالي الطلب"
    )
    address = models.CharField(
        max_length=255,
        verbose_name="عنوان التوصيل"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الطلب"
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "قيد الانتظار"),
            ("paid", "تم الدفع"),
            ("shipped", "تم الشحن"),
            ("delivered", "تم التوصيل"),
        ],
        default="pending",
        verbose_name="حالة الطلب"
    )

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"

    def __str__(self):
        return f"طلب رقم {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="الطلب"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="المنتج"
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name="الكمية"
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="السعر"
    )

    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلب"

    def __str__(self):
        return self.product.name
