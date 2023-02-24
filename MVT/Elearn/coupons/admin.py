from django.contrib import admin
from .models import Coupon
from django.utils.timesince import timesince
from django.utils import timezone

# Register your models here.
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'time_until_expired', 'starts', 'ends', 'duration', 'active']
    list_filter = ['active', 'starts', 'ends']
    search_fields = ['code',]
    ordering = ['starts', 'ends']
    
    def duration(self, obj):
        delta = obj.ends - obj.starts
        return delta
    
    def time_until_expired(self, obj):
        if obj.active:           
            now = timezone.now()
            if obj.ends <= now:
                return 'Expired'
            else:
                delta = obj.ends - now
                days = delta.days
                hours = delta.seconds // 3600
                minutes = (delta.seconds // 60) % 60
                if days > 0:
                    return f"{days}d {hours}h {minutes}m"
                elif hours > 0:
                    return f"{hours}h {minutes}m"
                else:
                    return f"{minutes}m"
        else:
            return 'Coupon is not active'
