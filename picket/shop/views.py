from django.shortcuts import render
from products.models import Product

def index(request):
    products = Product.objects.filter(available = True)
    return render(request, 'shop/index.html', {
        'products': products
    })
