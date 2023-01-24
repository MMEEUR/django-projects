from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Category, Product
# Create your views here.

def productListView(request, cat_slug=None):
    category = None
    categories = Category.objects.all()
    object_list = Product.objects.filter(available=True)
    total_products = Product.objects.count()
    
    if cat_slug:
        category = get_object_or_404(Category, slug=cat_slug)
        object_list = object_list.filter(category=category)
        
    paginator = Paginator(object_list, 4)
    page = request.GET.get('page')
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        
    return render(request, 'shop/product_list.html', {'category': category, 'categories': categories, 'products': products, 'total_products': total_products})

def productDetailView(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    
    return render(request, 'shop/product_detail.html', {'product': product})
