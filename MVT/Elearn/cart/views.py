from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from shop.models import Product
from .forms import CartAddForm
from coupons.forms import CouponApplyForm
from .cart import Cart

# Create your views here.
@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart_form = CartAddForm(request.POST)
    
    if cart_form.is_valid():
        cd = cart_form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
        
    return redirect("cart:cart_detail")

@require_POST
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request) 
    cart.remove(product=product)
    
    return redirect("cart:cart_detail")

def cart_detail(request):
    cart = Cart(request)
    form = CouponApplyForm()
    for item in cart:
        item['update_quantity_form'] = CartAddForm(initial={'quantity': item['quantity'], 'override': True})
    
    return render(request, 'cart/cart_detail.html', {'cart': cart, 'form': form})
