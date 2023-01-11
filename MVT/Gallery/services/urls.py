from django.urls import path
from .views import servicesView

app_name = 'services'

urlpatterns = [
    path('', servicesView, name='services'),
]
