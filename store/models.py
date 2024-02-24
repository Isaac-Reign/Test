from django.db import models
from django.urls import reverse


class ProductCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    application_area = models.TextField()
    suitable_production_process = models.TextField()
    characteristics = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('products')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ("-created",)
        verbose_name_plural = "Products Categories"


class Product(models.Model):
    STATUS_CHOICES = [
        ('DRAFT', "Draft"),
        ('PUBLISHED', 'Published'),
    ]
    name = models.CharField(max_length=250)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    description = models.TextField()
    slug = models.SlugField()
    image_one = models.ImageField(verbose_name="First Image")
    image_two = models.ImageField(null=True, blank=True, verbose_name="Second Image")
    image_three = models.ImageField(null=True, blank=True, verbose_name="Third Image")
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    published_on = models.DateTimeField(auto_now=True, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="DRAFT")
    
    def get_absolute_url(self):
        return reverse('product_details', kwargs={'slug': self.slug})
    def __str__(self):
        if self.status == "PUBLISHED":
            return self.name
        else:
            return f">>>>>{self.status}<<<<<{self.name}"
    class Meta:
        ordering = ("-published_on",)
        verbose_name_plural = "Products"

class Article(models.Model):
    STATUS_CHOICES = [
        ('DRAFT', "Draft"),
        ('PUBLISHED', 'Published'),
    ]
    title = models.CharField(max_length=200)
    header = models.CharField(max_length=250, blank=True, null=True, help_text="Optinal")
    slug = models.SlugField()
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True,  blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="DRAFT")
    def get_absolute_url(self):
        return reverse('news_details', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class ArticleSection(models.Model):
    header = models.CharField(max_length=250, blank=True, null=True, help_text="Optinal")
    content = models.TextField()
    section = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f"Article: {self.section}...Header: {self.header}...content{self.content}"