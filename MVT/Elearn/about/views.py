from django.shortcuts import render
from shop.models import Product
from teacher.models import Teacher

# Create your views here.
def about_us(request):
    teachers = Teacher.objects.all()
    total_students = 0
    total_courses = Product.objects.all().count()
    
    for i in Product.objects.all():
        total_students += i.students
        
    context = {
        'teachers': teachers,
        'total_students': total_students,
        'total_courses': total_courses
    }
        
    return render(request, 'about/about_us.html', context=context)
