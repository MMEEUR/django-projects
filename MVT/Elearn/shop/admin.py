from django.contrib import admin
from .models import Product, Category, Lecture, Review

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available')
    list_filter = ('available', 'created')
    ordering = ('available', 'created')
    raw_id_fields = ('category',)
    search_field = ('name',)
    prepopulated_fields = {'slug':('name',)}
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug':('name',)}
    search_field = ('name',)
    
@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('course', 'id', 'name')
    list_filter = ('course',)
    ordering = ('course', 'id')
    raw_id_fields = ('course',)
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'created', 'active')
    list_filter = ('active',)
    ordering = ('active', '-created')
    search_field = ('first_name', 'last_name', 'comment')
