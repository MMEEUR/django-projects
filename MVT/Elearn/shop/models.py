from django.db import models
from django.urls import reverse
from teacher.models import Teacher

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ('name',)
        
    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])
        
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m', blank=True)
    summery = models.CharField(max_length=250)
    requirements = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duaration = models.DurationField()
    quizzes = models.IntegerField()
    students = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        index_together = (('id'), ('slug'),)
        
    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])
    
    def __str__(self):
        return self.name
    
class Lecture(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    duaration = models.DurationField()
    course = models.ForeignKey(Product, related_name='lectures', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ('course','id')
    
    def __str__(self):
        return f'{self.course}-{self.id}-{self.name}'
