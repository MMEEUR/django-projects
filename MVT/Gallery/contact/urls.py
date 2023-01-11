from django.urls import path
from .views import contactView, contactDoneView

app_name = 'contact'

urlpatterns = [
    path('', contactView, name='contact_us'),
    path('done', contactDoneView, name='contact_done'),
]
