from django.urls import path
from .views import aboutView

app_name = 'about'

urlpatterns = [
    path('', aboutView, name='about_us'),
]
