from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, editable=False)
    
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("blog:post_list_by_cat", args=[self.slug])

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/%Y/%m/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('title',)
    
    def __str__(self):
        return self.title
    
    def comments_count(self):
        return self.comments.filter(active=True).count()
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.id])

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    author = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    
    class Meta:
        ordering = ('-created_at',)
    
    def __str__(self):
        return f'{self.id}. {self.text}'
