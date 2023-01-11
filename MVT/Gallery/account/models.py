from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    STATUS_CHOICES = (
        ('manager', 'مدیر'),
        ('developer', 'توسعه‌دهنده'),
        ('designer', 'طراح پروژه'),
    )
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio  = models.CharField(max_length=50, blank=True)
    task = models.CharField(choices=STATUS_CHOICES, max_length=20, blank=True, null=True, default=None)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/photos/%Y/%m/%d/', blank=True)
    
    def __str__(self):
        return f'{self.user.get_full_name()}'