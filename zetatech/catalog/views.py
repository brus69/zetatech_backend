from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .models import Product, CategoryProduct
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def get_sidebar_categories():
    return CategoryProduct.objects.all()


def product(request, slug=None):
    tovar = Product.objects.all()
    paginator = Paginator(tovar, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    sidebar = get_sidebar_categories()
    if slug is not None:
        category = get_object_or_404(CategoryProduct, slug=slug)
        tovar = tovar.filter(catalog=category)
    context = {
        'tovar': tovar,
        'sidebar': sidebar,
        'page_obj': page_obj
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

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['brus739@gmail.com'])
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        return HttpResponseRedirect('/')
    else:
        return HttpResponse("Make sure all fields are entered and valid.")
