from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product, CategoryProduct
# Create your views here.

def get_sidebar_categories():
    return CategoryProduct.objects.all()


def product(request, slug=None):
    tovar = Product.objects.all()
    sidebar = get_sidebar_categories()
    if slug is not None:
        category = get_object_or_404(CategoryProduct, slug=slug)
        tovar = tovar.filter(catalog=category)
    context = {
        'tovar': tovar,
        'sidebar': sidebar,
    }
    return render(request, 'product/product.html', context)


def product_detail(request, product_slug):
    tovar = get_object_or_404(Product, slug=product_slug)
    sidebar = get_sidebar_categories()
    context = {
        'tovar': tovar,
        'sidebar': sidebar,
    }
    return render(request, 'product/product_detail.html', context)