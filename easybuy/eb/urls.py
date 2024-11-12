# eb/urls.py
from django.urls import path
from easybuy import views

urlpatterns = [
    path('', views.main, name='main'),
    path('category/<int:category_id>/', views.category_products, name='category_products'),
    path('electric/', views.electric, name='electric'),
]
