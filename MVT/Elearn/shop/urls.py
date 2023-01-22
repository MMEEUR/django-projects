from django.urls import path, register_converter
from django.urls.converters import SlugConverter
from .views import productDetailView, productListView

app_name = 'shop'

class PersianSlugConvertor(SlugConverter):
    regex = '[-a-zA-Z0-9_ضصثقفغعهخحجچگکمنتالبیسشظطزژرذدپوءآ]+'
    
register_converter(PersianSlugConvertor, 'persian_slug')

urlpatterns = [
    path('', productListView, name='product_list'),
    path('<persian_slug:category_slug', productListView, name='product_list_by_category'),
    path('<int:id>/<persian_slug:slug>', productDetailView, name='product_detail'),
]
