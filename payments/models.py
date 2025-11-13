from django.db import models
from orders.models import Order

class Payment(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name="الطلب"
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="المبلغ"
    )
    method = models.CharField(
        max_length=50,
        verbose_name="طريقة الدفع"  # مثل ApplePay, Card, Mada
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "قيد الانتظار"),
            ("success", "ناجح"),
            ("failed", "فشل"),
        ],
        default="pending",
        verbose_name="حالة الدفع"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ العملية"
    )

    class Meta:
        verbose_name = "دفعة"
        verbose_name_plural = "المدفوعات"

    def __str__(self):
        return f"دفع للطلب {self.order.id}"
