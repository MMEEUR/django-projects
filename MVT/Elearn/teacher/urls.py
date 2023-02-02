from django.urls import path
from .views import teacherListView, teacherDetailView

app_name = 'teacher'

urlpatterns = [
    path('', teacherListView, name='teacher_list'),
    path('<slug:slug>', teacherDetailView, name='teacher_detail')
]
