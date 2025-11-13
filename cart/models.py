from django.db import models
from catalog.models import Product

class CartItem(models.Model):
    session_key = models.CharField(
        max_length=255,
        verbose_name="مُعرّف الجلسة"
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

    class Meta:
        verbose_name = "عنصر في السلة"
        verbose_name_plural = "عناصر السلة"

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    def total_price(self):
        return self.product.price * self.quantity
