from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.TextField(max_length=50)
    slug = models.TextField(max_length=50)
    biography = models.CharField(max_length=150)
    about = models.TextField(max_length=250)
    about = models.TextField(max_length=250)
    achievements = models.TextField(max_length=250)
    objectives = models.TextField(max_length=250)
    role = models.CharField(max_length=20)
    
    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name
