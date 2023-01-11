from django.contrib import admin
from .models import Project

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image1', 'created', 'id']
    prepopulated_fields = {'slug':('title',)}
    list_filter = ['created']