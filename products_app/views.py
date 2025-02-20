from django.shortcuts import render
from .models import Product

# Create your views here.
def products_page(request):
    products = Product.objects.all()
    return render(request, 'products_app/products.html', {'products': products})