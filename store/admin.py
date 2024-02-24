from django.contrib import admin
from .models import ProductCategory, Product, Article, ArticleSection

admin.site.site_header = "Shen Yun Website Administrator!"

class ProductAdmin(admin.ModelAdmin):
    exclude = ("slug",)

class ArticleAdmin(admin.ModelAdmin):
    exclude = ("slug",)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleSection)