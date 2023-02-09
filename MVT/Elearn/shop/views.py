from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.csrf import csrf_exempt
from .models import Category, Product
from .forms import ReviewForm
# Create your views here.

def product_list_view(request, cat_slug=None):
    category = None
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
        
    return render(request, 'shop/product_list.html', {'category': category, 'products': products, 'products_count': products_count})

def product_detail_view(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    product_lectures = product.lectures.all()
    product_reviews = product.reviews.filter(active=True).order_by('-created')
    latest_products = Product.objects.filter(available=True).exclude(id=product.id)[:3]
    releted_products = Product.objects.filter(category=product.category, available=True).exclude(id=product.id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect(product.get_absolute_url())
    else:
        form = ReviewForm(initial={'course': product})
    
    return render(request, 'shop/product_detail.html', {'product': product, 'form': form, 'product_reviews': product_reviews, 'releted_products': releted_products, 'product_lectures': product_lectures, 'latest_products': latest_products})
