from django.shortcuts import render
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem

# Create your views here.
def order_create(request):
    cart = Cart(request)
    
    if request.method == 'POST':
        order_form = OrderCreateForm(data=request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            cart.clear()
            
            return render(request, 'orders/order_created.html', {'order': order})
    else:
        order_form = OrderCreateForm()
        
    return render(request, 'orders/order_create.html', {'cart': cart, 'order_form': order_form})
