# eb/views.py
from django.shortcuts import render, get_object_or_404

from .models import Category, Product

def main(request):
    Categories = Category.objects.all()
    context = {'Categories': Categories}
    return render(request, 'eb/main.html', context)

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'eb/electric.html', {'category': category, 'products': products})

def electric(request):
    return render(request, 'eb/electric.html', {})
