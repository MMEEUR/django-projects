from django.urls import path, register_converter
from django.urls.converters import SlugConverter
from .views import projectView, projectDetailView

app_name = 'projects'

class PersianSlugConvertor(SlugConverter):
    regex = '[-a-zA-Z0-9_ضصثقفغعهخحجچگکمنتالبیسشظطزژرذدپوءآ]+'
    
register_converter(PersianSlugConvertor, 'persian_slug')

urlpatterns = [
    path('', projectView, name='projects'),
    path('<int:year>/<int:month>/<int:day>/<persian_slug:slug>', projectDetailView, name='projects_detail'),
]
