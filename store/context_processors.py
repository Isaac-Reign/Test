from .models import ProductCategory
import random


def base(request):
    path = ["store/images/default/display1.jpg", "store/images/default/display3.jpg",
                    "store/images/default/display4.jpg", "store/images/default/display5.jpg", 
                    "store/images/default/display6.jpg", "store/images/default/display7.jpg", 
                    "store/images/default/display8.jpg"]
    random_img = random.choice(path)

    product_catalogues = ProductCategory.objects.all()
    return {"product_catalogues": product_catalogues, "random_img": random_img}