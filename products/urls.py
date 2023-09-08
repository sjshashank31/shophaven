"""
URL configuration for ShopHaven project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views

app_label = "product"

urlpatterns = [
    path('', views.ProductListing.as_view(), name="product-listing"),
    path('<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name="add-to-cart"),
    path('cart/', login_required(views.CartListing.as_view()), name='cart-listing'),
    path('remove-item-from-cart/<int:pk>/', views.remove_item_from_cart, name="remove-item-from-cart")

]
