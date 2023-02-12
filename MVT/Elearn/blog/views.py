from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Sum
from .models import Post, Category
from .forms import CommentForm, ReplyForm

def post_list_view(request, cat_slug=None):
    object_list = Post.objects.filter(active=True)
    categories = Category.objects.all()
    popular_posts = object_list.annotate(comment_sum=Sum('comments__replies__id')).order_by('-comment_sum')[:3]
    category = None
    
    if cat_slug:
        category = get_object_or_404(categories, slug=cat_slug)
        object_list = Post.objects.filter(category=category)
        
    paginator = Paginator(object_list, 2)
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    context = {
        'posts': posts,
        'categories': categories,
        'category': category,
        'popular_posts': popular_posts,
    }    

    return render(request, 'blog/post_list.html', context=context)

def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.filter(active=True)
    popular_posts = Post.objects.annotate(comment_sum=Sum('comments__replies__id')).order_by('-comment_sum')[:3]
    
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        reply_form = ReplyForm(data=request.POST)
        
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            
            return redirect(post.get_absolute_url())
        
        elif reply_form.is_valid():
            new_reply = reply_form.save(commit=False)
            new_reply.save()
            
            return redirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()
        reply_form = ReplyForm()
        
    context = {
        'post': post,
        'popular_posts': popular_posts,
        'comments': comments,
        'comment_form': comment_form,
        'reply_form': reply_form,
    }    
    
    return render(request, 'blog/post_detail.html', context=context)
