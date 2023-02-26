from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone
from .forms import CouponApplyForm
from .models import Coupon

# Create your views here.
@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(data=request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code, starts__lte=now, ends__gte=now, active=True)
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = coupon.id
            
    return redirect('cart:cart_detail')
