from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Teacher

# Create your views here.
def teacher_list_view(request):
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

def teacher_detail_view(request, slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    teacher_courses = teacher.courses.all()
    
    return render(request, 'teacher/teacher_detail.html', {'teacher': teacher, 'teacher_courses': teacher_courses})
