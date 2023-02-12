from django.urls import path
from .views import post_list_view, post_detail_view

app_name = 'blog'

urlpatterns = [
    path('', post_list_view, name='post_list'),
    path('<int:post_id>', post_detail_view, name='post_detail'),
    path('<slug:cat_slug>', post_list_view, name='post_list_by_cat'),
]
