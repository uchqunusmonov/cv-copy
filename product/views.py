from django.shortcuts import render
from .models import Brand, Products
# Create your views here.

def brand(request):
    brands = Brand.objects.all()

    products = Products.objects.all()
    context = {
        'brands':brands,
        'products':products
    }
    return render(request, 'product.html', context)

def product_details(request, slug):
    product = Products.objects.get(slug=slug)
    context = {
        'product':product
    }
    return render(request, 'product-details.html', context)