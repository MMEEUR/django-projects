from django.contrib import admin
from .models import Post, Category, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'created_at', 'updated_at', 'active')
    list_filter = ('active', 'category')
    ordering = ('active', '-created_at')
    raw_id_fields = ('category',)
    search_fields = ('title', 'content', 'author')
    
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    ordering = ('name',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'parent', 'created_at', 'active')
    list_filter = ('active',)
    ordering = ('active', 'parent', '-created_at')
    search_fields = ('author', 'text', 'post', 'parent')
