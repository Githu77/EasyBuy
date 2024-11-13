# eb/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Category, Product
from django.db.models import Q

def main(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'eb/main.html', context)

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    categories = Category.objects.all()
    products = Product.objects.filter(category=category)
    return render(request, 'eb/electric.html', {'category': category, 'products': products, 'categories': categories})

def electric(request):
    return render(request, 'eb/electric.html', {})



def product_search(request):
    query = request.GET.get('q')  # Get the search query from the request
    products = Product.objects.all()  # Start with all products
    categories = Category.objects.all()
    
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
    }
    return render(request, 'eb/search.html', context)

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if product already in cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return JsonResponse({'total_items': cart.total_items})

@login_required
def view_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return render(request, 'easybuy/cart.html', {'cart': cart})

# easybuy/views.py (Add stock availability check in add_to_cart)

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.stock_quantity < 1:
        return JsonResponse({'error': 'This item is out of stock'}, status=400)

    # Rest of the function remains the same
