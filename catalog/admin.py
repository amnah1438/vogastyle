from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, ProductImage


# ============================
# التصنيفات مع عرض صورة مصغرة
# ============================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image_tag')
    prepopulated_fields = {'slug': ('name',)}

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit:cover; border-radius:6px;" />',
                obj.image.url
            )
        return "—"
    image_tag.short_description = "الصورة"


# ============================
# Inline الصور الإضافية للمنتج
# ============================
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="80" height="80" style="object-fit:cover; border-radius:6px;" />',
                obj.image.url
            )
        return "—"
    preview.short_description = "معاينة"


# ============================
# المنتجات مع صورة رئيسية
# ============================
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'created_at', 'main_image_tag')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]

    def main_image_tag(self, obj):
        if obj.main_image:
            return format_html(
                '<img src="{}" width="70" height="70" style="object-fit:cover; border-radius:8px;" />',
                obj.main_image.url
            )
        return "—"
    main_image_tag.short_description = "الصورة الرئيسية"


# ============================
# الصور الإضافية — عرض المنتج فقط
# ============================
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit:cover; border-radius:6px;" />',
                obj.image.url
            )
        return "—"
    image_preview.short_description = "الصورة"
