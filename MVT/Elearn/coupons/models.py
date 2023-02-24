from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    starts = models.DateTimeField()
    ends = models.DateTimeField()
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.code
    
    def clean(self):
        super().clean()

        if self.starts and self.ends and self.starts > self.ends:
            raise ValidationError('Start time cannot be later than end time.')
