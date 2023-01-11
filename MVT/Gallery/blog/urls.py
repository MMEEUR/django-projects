from django.urls import path, register_converter
from django.urls.converters import SlugConverter
from . import views

app_name = 'blog'

class PersianSlugConvertor(SlugConverter):
    regex = '[-a-zA-Z0-9_ضصثقفغعهخحجچگکمنتالبیسشظطزژرذدپوءآ]+'
    
register_converter(PersianSlugConvertor, 'persian_slug')

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('search', views.post_search, name='post_search'),
    path('tag/<persian_slug:tag_slug>', views.post_list, name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<persian_slug:slug>', views.post_detail, name='post_detail'),
]
