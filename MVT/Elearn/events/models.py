from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, editable=False)
    content = models.TextField()
    image = models.ImageField(upload_to='events/%Y/%m/')
    event_day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    place = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('title',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("events:event_detail", args=[self.event_day, self.slug])
    
    def date(self):
        return f'{self.event_day.year}/{self.event_day.month}/{self.event_day.day}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
