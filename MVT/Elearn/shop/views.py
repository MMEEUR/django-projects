from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Category, Product
# Create your views here.

def productListView(request, cat_slug=None):
    category = None
    categories = Category.objects.all()
    object_list = Product.objects.filter(available=True)
    
    if cat_slug:
        category = get_object_or_404(Category, slug=cat_slug)
        object_list = object_list.filter(category=category)
    
    products_count = object_list.count()
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        
    return render(request, 'shop/product_list.html', {'category': category, 'categories': categories, 'products': products, 'products_count': products_count})

def productDetailView(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    releted_products = Product.objects.filter(category=product.category).exclude(id=product.id)
    
    return render(request, 'shop/product_detail.html', {'product': product, 'releted_products': releted_products})
