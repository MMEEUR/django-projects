from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Teacher
from shop.models import Product


# Create your views here.
def teacherListView(request):
    object_list = Teacher.objects.all()
    
    paginator = Paginator(object_list, 4)
    page = request.GET.get('page')
    
    try:
        teachers = paginator.page(page)
    except PageNotAnInteger:
        teachers = paginator.page(1)
    except EmptyPage:
        teachers = paginator.page(paginator.num_pages)
        
    return render(request, 'teacher/teacher_list.html', {'teachers': teachers})

def teacherDetailView(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    teacher_courses = Product.objects.filter(teacher=teacher)
    
    return render(request, 'teacher/teacher_detail.html', {'teacher': teacher, 'teacher_courses': teacher_courses})
