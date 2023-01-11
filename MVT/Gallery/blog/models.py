from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
from account.models import Profile

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'چرک نویس'),
        ('published', 'منتشر شده'),
    )
    
    title                = models.CharField(max_length=100)
    slug                 = models.SlugField(max_length=100, unique_for_date='publish', allow_unicode=True)
    body                 = models.TextField()
    author               = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    bolded_text          = models.TextField(blank=True)
    picture              = models.ImageField(upload_to='blog/photos/%Y/%m/%d/', blank=True)
    publish              = models.DateTimeField(default=timezone.now)
    created              = models.DateTimeField(auto_now_add=True)
    updated              = models.DateTimeField(auto_now=True)
    status               = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tags                 = TaggableManager()
    
    objects = models.Manager()
    published = PublishedManager()
    
    class Meta:
        ordering = ('-publish',)
        
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post                = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    profile             = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_comments')
    body                = models.TextField()
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)
    active              = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('created',)
        
    def __str__(self):
        return f'نظر توسط {self.profile} در {self.post}'    

#class Comment(models.Model):
#    post                = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#
#    name                = models.CharField(max_length=80)
#    email               = models.EmailField()
#    body                = models.TextField()
#    created             = models.DateTimeField(auto_now_add=True)
#    updated             = models.DateTimeField(auto_now=True)
#    active              = models.BooleanField(default=False)
    
#    class Meta:
#       ordering = ('created',)
        
#    def __str__(self):
#        return f'نظر توسط {self.name} در {self.post}'