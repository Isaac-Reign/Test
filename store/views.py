from django.shortcuts import render
from .models import Product, Article, ArticleSection
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.views.decorators.cache import cache_page

def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Server-side validation
        if not name or not email or not phone or not message:
            return JsonResponse({'success': False, 'message': 'Please fill in all fields.'})

        # Send email to yourself
        try:
            send_mail(
                'New Contact Form Submission',
                f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}',
                f'{email}',
                ['shenyunnewmaterials@gmail.com'],
                fail_silently=False,
            )
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'An error occurred while sending the email: {str(e)}'})

        # Send confirmation email to the user
        try:
            send_mail(
                'Contact Form Submission Confirmation',
                'Thank you for contacting us. Your email has been received and will be reviewed.',
                'shenyunnewmaterials@gmail.com',
                [email],
                fail_silently=False,
            )
        except Exception as e:
            return JsonResponse({'success': False, 'message': f'An error occurred while sending the confirmation email: {str(e)}'})

        return JsonResponse({'success': True, 'message': 'Email sent successfully.'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method.'})
        

# @cache_page(60 * 15)
def home(request):
    products = Product.objects.filter(status="PUBLISHED").order_by("?")[:9]
    
    articles = Article.objects.filter(status="PUBLISHED")[:3]
    context = {"products": products, "articles": articles}
    return render(request, "store/index.html", context)

def products(request):
    q = request.GET.get('q', '')
    page = request.GET.get("page")
    
    products = Product.objects.filter(
        Q(status='PUBLISHED') &
        (Q(name__icontains=q)|
        Q(product_category__name__icontains=q)|
        Q(slug__icontains=q))
    )


    paginator = Paginator(products, 9)
    try:
        query = paginator.page(page)
    except PageNotAnInteger:
        query = paginator.page(1)
    except EmptyPage:
        query = paginator.page(paginator.num_pages)
    
    context = {'query': query, "q": q}
    return render(request, "store/shop.html", context)

def product_details(request, slug):
    import random
    item = Product.objects.filter(slug__iexact=slug, status='PUBLISHED')
    
    if item.exists():
        item = item.first()
    else:
        return HttpResponse('<h1>Product Not Found <a href="/products/">View all Products</a></h1>')


    comments = random.randint(44, 250)
    rate = round(random.uniform(4.8, 5.0), 1)
 
    related_catalogue_name = item.product_category.name
    related_products = Product.objects.filter(product_category__name=related_catalogue_name, status='PUBLISHED').exclude(slug__iexact=slug).order_by('?')    
    none_related = Product.objects.filter(status='PUBLISHED').exclude(product_category__name=related_catalogue_name).order_by("?")[:8]

    context = {'item': item, "related_products": related_products, "none_related": none_related, "comments": comments, "rate": rate}
    return render(request, "store/shop-single.html", context)

def news(request):
    articles = Article.objects.filter(status="PUBLISHED")
    paginator = Paginator(articles, 12)
    page = request.GET.get('page')
    try:
        paginator = paginator.page(page)
    except PageNotAnInteger:
        paginator = paginator.page(1)
    except EmptyPage:
        paginator = paginator.page(paginator.num_pages)

    context = {"paginator": paginator}
    return render(request, "store/news.html", context)

def news_details(request, slug):
    import random
    item = Article.objects.filter(slug__iexact=slug, status='PUBLISHED')
    if item.exists():
        item = item.first()
    else:
        return HttpResponse('<h1>Article Not Found <a href="/articles/">View all Articles</a></h1>')
        # ComeBack
    item_section = ArticleSection.objects.filter(section__title=item.title)
    related_articles = Article.objects.all().exclude(status="DRAFT").exclude(slug=item.slug).order_by("?")[:4]
    views = random.randint(42, 1200)

    context = {"item": item, "item_section": item_section, "related_articles": related_articles, "views": views}
    return render(request, "store/news-single.html", context)

def about(request):
    context = {}
    return render(request, "store/about.html", context)


def coustom404(request, exception):
    return render(request, "404.html", status=404)

