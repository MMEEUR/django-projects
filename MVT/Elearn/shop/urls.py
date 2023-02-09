from django.urls import path, register_converter
from django.urls.converters import SlugConverter
from .views import product_detail_view, product_list_view

app_name = 'shop'

class PersianSlugConvertor(SlugConverter):
    regex = '[-a-zA-Z0-9_ضصثقفغعهخحجچگکمنتالبیسشظطزژرذدپوءآ]+'
    
register_converter(PersianSlugConvertor, 'persian_slug')

urlpatterns = [
    path('', product_list_view, name='product_list'),
    path('<persian_slug:cat_slug>', product_list_view, name='product_list_by_category'),
    path('<int:id>/<persian_slug:slug>', product_detail_view, name='product_detail'),
]
