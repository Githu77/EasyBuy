# eb/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Category, Product, Cart, CartItem, Order
from django.db.models import Q
import paypalrestsdk
from .paypal_config import paypalrestsdk
from django.urls import reverse

def main(request):
    categories = Category.objects.all()
    category_products = {}
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_items = sum(item.quantity for item in cart_items)
    # Fetch top 5 popular products in each category
    for category in categories:
        top_products = Product.objects.filter(category=category).order_by('-popularity')[:3]
        category_products[category] = top_products

    context = {
        'category_products': category_products,
        'categories': categories,
        'total_items': total_items
    }
    return render(request, 'eb/main.html', context)


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    categories = Category.objects.all()
    products = Product.objects.filter(category=category)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_items = sum(item.quantity for item in cart_items)
    
    return render(request, 'eb/products.html', {
        'category': category,
        'products': products,
        'categories': categories,
        'total_items': total_items
        })

def products(request):
    return render(request, 'eb/products.html', {})



def product_search(request):
    query = request.GET.get('q')  # Get the search query from the request
    products = Product.objects.all()  # Start with all products
    categories = Category.objects.all()
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    #Retrieve total items
    total_items = sum(item.quantity for item in cart_items)
    
    if query:
        # Use Q to search across multiple fields
        products = products.filter(
            Q(name__icontains=query) |  # Search by product name
            Q(description__icontains=query)  # Search by product description
        )

    context = {
        'products': products,
        'query': query,
        'categories': categories,
        'total_items': total_items
    }
    return render(request, 'eb/search.html', context)

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    #Retrieve total items
    total_items = sum(item.quantity for item in cart_items)
    context = {
        'product': product,
        'categories': categories,
        'total_items': total_items
        
    }
    return render(request, 'eb/productdetails.html', context)

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    # Check product availability
    if product.stock_quantity < 1:
        return JsonResponse({'error': 'This item is out of stock'}, status=400)
    # Check if product already in cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    
    # Increment product popularity
    product.popularity += 1
    product.save()

    return JsonResponse({
        'total_items': cart.total_items,
        'product_id': product_id,
    })


@login_required
def view_cart(request):
    # Get or create a cart for the logged-in user
    cart, _ = Cart.objects.get_or_create(user=request.user)
    
    # Retrieve all cart items associated with the cart
    cart_items = CartItem.objects.filter(cart=cart)

    #Retrieve all categories
    categories = Category.objects.all()
    
    #Retrieve total items
    total_items = sum(item.quantity for item in cart_items)
    
    # Calculate total price for each cart item
    for item in cart_items:
        item.total_price = item.product.price * item.quantity
    
    # Prepare context for rendering the template
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'categories': categories,
        'total_items': total_items
    }
    
    # Render the cart template with the context
    return render(request, 'eb/cart.html', context)
# easybuy/views.py (Add stock availability check in add_to_cart)

@login_required
def remove_from_cart(request, product_id):
    cart = Cart.objects.get(user=request.user)
    cart_item = cart.items.filter(product_id=product_id).first()

    if cart_item:
        cart_item.delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Item not found in cart'}, status=404)
    

@login_required
def checkout(request):
    order, created = Order.objects.get_or_create(user=request.user, is_paid=False)
    categories = Category.objects.all()
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_items = sum(item.quantity for item in cart_items)
    
    # Calculate total for each item and overall total price
    for item in cart_items:
        item.total_price = item.product.price * item.quantity

    order.total_price = sum(item.total_price for item in cart_items)
    order.save()

    if request.method == 'POST':
        order.is_paid = True
        order.save()
        
        for item in order.items.all():
            item.product.stock_quantity -= item.quantity
            item.product.save()

        return redirect('order_success')

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'categories': categories,
        'total_items': total_items,
        'total_price': order.total_price,
    }
    
    return render(request, 'eb/checkout.html', context)


def create_payment(request):
    # Example items for testing
    items = [
        {
            "name": "Sample Product",
            "sku": "12345",
            "price": "10.00",
            "currency": "USD",
            "quantity": 1,
        }
    ]

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url": request.build_absolute_uri(reverse('execute_payment')),
            "cancel_url": request.build_absolute_uri(reverse('checkout'))},
        "transactions": [{
            "item_list": {"items": items},
            "amount": {
                "total": "10.00",  # Calculate the total dynamically
                "currency": "USD"},
            "description": "Payment for items in cart"}]})

    if payment.create():
        # Redirect user to PayPal for payment approval
        for link in payment.links:
            if link.rel == "approval_url":
                return redirect(link.href)
    else:
        # Handle errors and redirect user back to cart/checkout page
        print(payment.error)
        return render(request, 'eb/payment_error.html')
    
    
# easybuy/views.py
def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')
    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        return render(request, 'eb/payment_success.html')
    else:
        return render(request, 'eb/payment_error.html', {"error": payment.error})
