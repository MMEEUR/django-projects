from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Project(models.Model):
    STATUS_CHOICES = (
        ('artists', 'هنری'),
        ('people', 'مردم'),
        ('travel', 'سفر'),
        ('poetic', 'شاعرانه'),
    )
    title = models.CharField(max_length=200)
    slug  = models.SlugField(max_length=200, allow_unicode=True)
    description = models.TextField()
    created = models.DateField(auto_now_add=True, db_index=True)
    customer = models.CharField(max_length=30)
    grouping = models.CharField(max_length=10, choices=STATUS_CHOICES, default='artists')
    place = models.CharField(max_length=30)
    rating = models.IntegerField(default=0)
    image1 = models.ImageField(upload_to='projects/photos/%Y/%m/%d/')
    image2 = models.ImageField(upload_to='projects/photos/%Y/%m/%d/')
    image3 = models.ImageField(upload_to='projects/photos/%Y/%m/%d/')
    image4 = models.ImageField(upload_to='projects/photos/%Y/%m/%d/')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_likes', blank=True)
    #url   = models.URLField()
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('projects:projects_detail', args=[self.created.year, self.created.month, self.created.day, self.slug])
    '''
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            
        super().save(*args, **kwargs)
    '''