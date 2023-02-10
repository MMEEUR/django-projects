from django.contrib import admin
from .models import Teacher, Review

# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    list_filter = ('role',)
    search_field = ('name',)
    prepopulated_fields = {'slug':('name',)}
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'rating', 'created', 'active')
    list_filter = ('active',)
    ordering = ('active', '-created')
    search_field = ('first_name', 'last_name', 'comment')
