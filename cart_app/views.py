from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .cart import Cart
from .models import Order, OrderItem

# Обработка страницы корзины с созданием объекта корзины и наполнением её списком продуктов
def cart(request):
    cart = Cart(request)
    cart_items = []
    for item in cart.get_items():
        total_price = float(item["product"].price) * item["quantity"]  # Вычисляем общую стоимость
        cart_items.append({
            "product": item["product"],
            "quantity": item["quantity"],
            "total_price": total_price  # Добавляем общую стоимость
        })
    context = {
        'cart': cart,
        'cart_items': cart_items,  # Передаем список товаров с общей стоимостью
        'cart_total_positions': cart.get_total_positions()
    }
    return render(request, 'cart_app/cart.html', context)

# Обработка POST запроса на добавление в корзину из карточки товара
@require_POST
def add_to_cart(request):
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity', 1))
    if not product_id:
        return JsonResponse({'success': False, 'error': 'Product ID is missing'}, status=400)
    
    cart = Cart(request)
    try:
        cart.add(product_id, quantity)
        return JsonResponse({
            'success': True,
            'total_items': cart.get_total_items(),
            'total_positions': cart.get_total_positions(),
            'summary': float(cart.get_summary())})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)
# Пост запрос на создание заказа только для авторизованных пользователей:
@login_required
def create_order(request):
    cart = Cart(request)
    order = Order.objects.create(user=request.user, total_cost=cart.get_summary())
    for item in cart.get_items():
        OrderItem.objects.create(order_id=order, product=item["product"], quantity=item["quantity"])
    cart.cart.clear()
    cart.save()
    return redirect('cart')