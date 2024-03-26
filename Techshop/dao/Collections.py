import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        # Check if product with the same ID already exists
        if any(p.product_id == product.product_id for p in self.products):
            raise ValueError("Product with the same ID already exists")
        self.products.append(product)

    def update_product(self, product_id, new_name, new_price, new_quantity):
        # Check if product exists
        for product in self.products:
            if product.product_id == product_id:
                # Update product details
                product.name = new_name
                product.price = new_price
                product.quantity = new_quantity
                return
        raise ValueError("Product not found")

    def remove_product(self, product_id):
        # Check if product exists
        for product in self.products:
            if product.product_id == product_id:
                # Check if the product has existing orders
                # For simplicity, assuming orders are managed elsewhere
                if product.quantity > 0:
                    raise ValueError("Cannot remove product with existing orders")
                self.products.remove(product)
                return
        raise ValueError("Product not found")

class Order:
    def __init__(self, order_id, customer_id, products):
        self.order_id = order_id
        self.customer_id = customer_id
        self.products = products
        self.status = "Pending"

    def update_status(self, new_status):
        self.status = new_status

class OrderManager:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        # Add order to the list
        self.orders.append(order)
        # Update inventory and payment records (not implemented here)

    def update_order_status(self, order_id, new_status):
        # Update order status
        for order in self.orders:
            if order.order_id == order_id:
                order.update_status(new_status)
                # Update inventory and payment records (not implemented here)
                return
        raise ValueError("Order not found")

    def cancel_order(self, order_id):
        # Cancel order and remove from the list
        for order in self.orders:
            if order.order_id == order_id:
                self.orders.remove(order)
                # Update inventory and payment records (not implemented here)
                return
        raise ValueError("Order not found")

class Order:
    def __init__(self, order_id, customer_id, products, order_date):
        self.order_id = order_id
        self.customer_id = customer_id
        self.products = products
        self.order_date = order_date

class OrderManager:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def sort_orders_by_date(self, ascending=True):
        self.orders.sort(key=lambda x: x.order_date, reverse=not ascending)

from sortedcontainers import SortedList

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = SortedList(key=lambda x: x.product_id)

    def add_product(self, product):
        # Check if product with the same ID already exists
        index = self.products.bisect_left(product)
        if index < len(self.products) and self.products[index].product_id == product.product_id:
            raise ValueError("Product with the same ID already exists")
        self.products.add(product)

    def update_product_quantity(self, product_id, new_quantity):
        # Find product by ID and update quantity
        for product in self.products:
            if product.product_id == product_id:
                product.quantity = new_quantity
                return
        raise ValueError("Product not found in inventory")

    def remove_product(self, product_id):
        # Remove product by ID
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                return
        raise ValueError("Product not found in inventory")
    
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def update_product_quantity(self, product_id, new_quantity):
        if product_id in self.products:
            self.products[product_id].quantity = new_quantity
        else:
            raise ValueError("Product not found in inventory")

    def decrement_product_quantity(self, product_id, quantity_to_decrement):
        if product_id in self.products:
            current_quantity = self.products[product_id].quantity
            if current_quantity >= quantity_to_decrement:
                self.products[product_id].quantity -= quantity_to_decrement
            else:
                raise ValueError("Insufficient stock")
        else:
            raise ValueError("Product not found in inventory")

class Product:
    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

class ProductCatalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def search_by_name(self, keyword):
        return [product for product in self.products if keyword.lower() in product.name.lower()]

    def search_by_category(self, category):
        return [product for product in self.products if category.lower() == product.category.lower()]

    def search_by_price_range(self, min_price, max_price):
        return [product for product in self.products if min_price <= product.price <= max_price]


class Product:
    def __init__(self, product_id, name, sku, price, quantity):
        self.product_id = product_id
        self.name = name
        self.sku = sku
        self.price = price
        self.quantity = quantity

class ProductCatalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        # Check for duplicates based on name or SKU
        if any(p.name == product.name or p.sku == product.sku for p in self.products):
            raise ValueError("Product with the same name or SKU already exists")
        self.products.append(product)

class PaymentRecord:
    def __init__(self, order_id, payment_id, amount, status):
        self.order_id = order_id
        self.payment_id = payment_id
        self.amount = amount
        self.status = status

class PaymentManager:
    def __init__(self):
        self.payments = []

    def record_payment(self, payment_record):
        self.payments.append(payment_record)

    def update_payment_status(self, order_id, new_status):
        for payment in self.payments:
            if payment.order_id == order_id:
                payment.status = new_status
                return
        raise ValueError("Payment record not found for the specified order ID")

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class OrderDetails:
    def __init__(self):
        self.details = []

    def add_detail(self, product, quantity):
        if product.quantity >= quantity:
            self.details.append({"product": product, "quantity": quantity})
            product.quantity -= quantity
        else:
            raise ValueError("Insufficient stock for product: {}".format(product.name))






