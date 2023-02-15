from django.contrib import admin
from .models import Event

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_day', 'start_time', 'end_time', 'place', 'address', 'active')
    list_filter = ('active',)
    ordering = ('event_day', 'start_time', 'end_time', 'active')
    search_fields = ('title', 'content', 'place', 'address')
