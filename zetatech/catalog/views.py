from django.shortcuts import render
from .models import Product
# Create your views here.

def product(request):
    tovar = Product.objects.all()
    return render(request, 'product/product.html', {'tovar':tovar})

def product_detail(request, slug):
    tovar_id = Product.objects.get(slug=slug)
    return render(request, 'product/product_detail.html', {'tovar_id': tovar_id})
