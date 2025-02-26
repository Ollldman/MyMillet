from django.conf import settings
from django.http import HttpRequest
from products_app.models import Product

class Cart:
    def __init__(self, request: HttpRequest):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product_id, quantity=1):
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 0, 
                "price": str(Product.objects.get(id=product_id).price)}
        self.cart[product_id]["quantity"] += quantity
        self.save()

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    def get_summary(self):
        summary = 0
        for item in self.cart.values():
            summary += item["quantity"] * float(item["price"])
        return summary

    def get_items(self):
        items = []
        for product_id, item in self.cart.items():
            product = Product.objects.get(id=int(product_id))
            items.append({
                "product": product, 
                "quantity": item["quantity"],
                "price": float(item["price"])
                })
        return items
    
    def get_total_items(self):
        total = 0
        for item in self.cart.values():
            total += item["quantity"]
        return total

    def get_total_positions(self):
        return len(self.cart)