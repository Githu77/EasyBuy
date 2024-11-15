# eb/urls.py
from django.urls import path
from easybuy import views

urlpatterns = [
    path('', views.main, name='main'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('products/', views.products, name='products'),
    path('search/', views.product_search, name='product_search'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('create-payment/', views.create_payment, name='create_payment'),
    path('execute-payment/', views.execute_payment, name='execute_payment'),
    path('checkout/', views.checkout, name='checkout'),
]
