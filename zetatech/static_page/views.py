from django.shortcuts import render
from .models import Faq, Team
from catalog.models import Product, CategoryProduct

# Create your views here.

team = Team.objects.all()

def index(request):
    exemple = Product.objects.all()
    context = {
        'team': team,
        'exemple': exemple,
    }
    return render(request, "static_page/index.html", context)

def faq(request):
    page = Faq.objects.all()
    context = {
        'page':page,
    }
    return render(request, 'static_page/faq.html', context)

def contact(request):
    return render(request, 'static_page/contact.html')

def offer(request):
    return render(request, "static_page/offer.html")

def page_not_found(request, exception):
    return render(request, 'static_page/404.html', {'path': request.path}, status=404)


