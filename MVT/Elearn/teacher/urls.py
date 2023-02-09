from django.urls import path
from .views import teacher_list_view, teacher_detail_view

app_name = 'teacher'

urlpatterns = [
    path('', teacher_list_view, name='teacher_list'),
    path('<slug:slug>', teacher_detail_view, name='teacher_detail')
]
