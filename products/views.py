from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Product, CartItem
from django.http import HttpResponseRedirect
# Create your views here.


class ProductListing(ListView):
    model = Product
    paginate_by = 100
    template_name = "product_list.html"
    queryset = Product.objects.get_available_products()


class ProductDetail(DetailView):
    model = Product
    template_name = "product_detail.html"


class CartListing(ListView):
    model = CartItem
    template_name = "cart_list.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = CartItem.objects.filter(user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_total'] = CartItem.objects.get_cart_total()
        print(context)
        return context

    def post(self, request, *args, **kwargs):
        print(self.request.POST)
        return HttpResponseRedirect('cart-list')


@login_required
def add_to_cart(request, **kwargs):
    product_id = kwargs.get('pk')
    user = request.user
    try:
        cart = CartItem.objects.get(user=user, product_id=product_id)
    except CartItem.DoesNotExist:
        cart = CartItem(user=user, product_id=product_id)

    cart.save()
    return HttpResponseRedirect(reverse('cart-listing'))

@login_required
def remove_item_from_cart(request, **kwargs):
    cart_item_id = kwargs.get("pk")
    try:
        item = CartItem.objects.get(id=cart_item_id)
        item.delete()
    except CartItem.DoesNotExist:
        print("item does not exist")

    return HttpResponseRedirect(reverse('cart-listing'))



