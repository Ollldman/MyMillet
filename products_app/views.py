from django.shortcuts import render
from .models import Product

# Create your views here.
def products_page(request):
    products = Product.objects.all()
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(request.session.session_key)
    return render(request, 'products_app/products.html', {'products': products})