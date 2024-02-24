from django.utils.text import slugify
from .models import Product, Article
import string
import random

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
    
def unique_slug_generator(instance, new_slug=None):
    slug = ""
    if isinstance(instance, Product):
        slug = slugify(instance.name)
    elif isinstance(instance, Article):
        slug = slugify(instance.title)

    if new_slug is not None:
        slug = new_slug
    # else:
    #     slug = slugify(instance.name)  # Assuming the name field is present on the Product model
    max_length = instance._meta.get_field('slug').max_length
    slug = slug[:max_length]
    Klass = type(instance)
    qs_exists = Klass.objects.filter(slug=slug).exists()
    
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug[:max_length-5], randstr=random_string_generator(size=4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
