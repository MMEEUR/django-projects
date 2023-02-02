from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='teachers/%Y/%m', null=True)
    biography = models.CharField(max_length=150)
    about = models.CharField(max_length=250)
    achievements = models.CharField(max_length=250)
    objectives = models.CharField(max_length=250)
    role = models.CharField(max_length=20)
    
    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name
