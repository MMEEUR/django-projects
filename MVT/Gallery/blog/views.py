from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity
from taggit.models import Tag
from .models import Post, Comment
from account.models import Profile
from .forms import CommentForm, SearchForm

# Create your views here.
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
    
def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tags = Tag.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        
    return  render(request, 'blog/post/list.html', {'posts': posts, 'tags': tags,})

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='published', publish__year=year, publish__month=month, publish__day=day)
    tags = Tag.objects.all()
    tagsList = []
    for tag in post.tags.get_queryset():
        tagsList.append(tag.name)
    inactive_comments = None
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        inactive_comments = post.comments.filter(active=False, profile=profile)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.profile = profile
            new_comment.post = post
            new_comment.save()
            
            return HttpResponseRedirect(request.path_info)#redirect('blog:post_detail',year=year, month=month, day=day, slug=post.slug)
    else:
        comment_form = CommentForm()
        
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:3]
        
    return render(request, 'blog/post/detail.html', {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form, 'similar_posts': similar_posts, 'tagsList': tagsList, 'tags': tags, 'inactive_comments':inactive_comments})

def post_search(request):
    tags = Tag.objects.all()
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            #results = Post.published.annotate(search=SearchVector('title', 'body'),).filter(search=query)
            #search_vector = SearchVector('title', 'body')
            #search_query  = SearchQuery(query)
            #results = Post.published.annotate(search=search_vector, rank=SearchRank(search_vector, search_query)).filter(search=search_query).order_by('-rank')
    
            #search_vector = SearchVector('title', weight='A') + SearchVector('body', weight='B')
            #search_query  = SearchQuery(query)
            #results = Post.published.annotate(search=search_vector, rank=SearchRank(search_vector, search_query)).filter(rank__gte=0.3).order_by('-rank')
            
            search_vector = SearchVector('title', weight='A') + SearchVector('body', weight='B')
            search_query  = SearchQuery(query)
            results = Post.published.annotate(similarity=TrigramSimilarity(expression='title', string=query),).filter(similarity__gt=0.1).order_by('-similarity')
            
    return render(request, 'blog/post/search.html', {'form': form, 'query': query, 'results': results, 'tags': tags})