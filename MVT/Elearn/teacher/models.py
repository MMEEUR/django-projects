from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

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
        
    def get_absolute_url(self):
        return reverse("teacher:teacher_detail", args=[self.slug])
        
    def __str__(self):
        return self.name
    
class Review(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='reviews')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
