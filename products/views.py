from django.shortcuts import render
from products.models import ProductCategory, Product


# Create your views here.

def index(request):
    context = {
        'title': 'geekShop'
    }
    return render(request, 'products/index.html', context)

def products(request):
    products_from_bd = Product.objects.all()
    categories_from_bd = ProductCategory.objects.all()

    context = {
        'title': 'GeekShop - Каталог',
        'products': products_from_bd,
        'categories': categories_from_bd,
    }
    return render(request, 'products/products.html', context)

