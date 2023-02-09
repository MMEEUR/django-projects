from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
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
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses', null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.CharField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m', blank=True)
    summery = models.CharField(max_length=250, null=True)
    requirements = models.CharField(max_length=250, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duaration = models.DurationField(null=True)
    quizzes = models.IntegerField(null=True)
    students = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        index_together = (('id'), ('slug'),)
        
    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])
    
    def average_rating(self):
        rating = []
        for i in self.reviews.filter(rating__isnull=False, active=True):
            rating.append(getattr(i, 'rating'))
            
        return sum(rating) / len(rating) if rating else 0
    
    def total_rating(self):
        return self.reviews.filter(active=True).count()
    
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
    
class Review(models.Model):
    course = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
