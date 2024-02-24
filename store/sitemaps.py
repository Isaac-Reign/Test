from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product, Article, ArticleSection


class HomeSitemap(Sitemap):
    protocol = 'http'
    changefrq = 'weekly'
    priority = 1.0,
    def items(self):
        return ['home']
    
    def location(self, item):
        return reverse(item)

class ProductsSitemap(Sitemap):
    protocol = 'http'
    changefrq = 'daily'
    priority = 1.0,
    def items(self):
        return ['products']
    def location(self, item):
        return reverse(item)

class ArticlesSitemap(Sitemap):
    protocol = 'http'
    changefrq = 'daily'
    priority = 1.0,
    def items(self):
        return ['news']

    def location(self, item):
        return reverse(item)
        
class SerieSitemap(Sitemap):
    protocol = 'http'
    def items(self):
        return Product.objects.filter(status='PUBLISHED')
    def lastmod(self, obj):
        return obj.created_on

class ArticleSitemap(Sitemap):
    protocol = 'http'
    def items(self):
        return Article.objects.filter(status='PUBLISHED')
    def lastmod(self, obj):
        return obj.updated