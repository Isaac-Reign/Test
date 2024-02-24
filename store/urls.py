from django.contrib.sitemaps.views import sitemap
from .sitemaps import  SerieSitemap, ArticleSitemap, HomeSitemap, ProductsSitemap, ArticlesSitemap
from .views import home, products, product_details, news, news_details, about, send_email
from django.urls import path
from django.views.generic.base import TemplateView

sitemaps = {
    'home': HomeSitemap,
    'products_sitemap': ProductsSitemap,
    'articles_sitemap': ArticlesSitemap,
    'series': SerieSitemap,
    'articles': ArticleSitemap,
}

urlpatterns = [
    path("", home, name='home'),
    path("products/", products, name='products'),
    path("products/<slug:slug>/", product_details, name='product_details'),
    path("articles/", news, name='news'),
    path("articles/details/<slug:slug>/", news_details, name='news_details'),
    path("about/", about, name='about'),
    path("send_email/", send_email, name='send_email'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'))
]