from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    
    UNIT = (
        ('pieces', 'Pieces'),
        ('meters', 'Meters'),
        ('dozen', 'Dozens'),
    )    
    
    name = models.CharField(max_length = 255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.CharField(max_length=20, choices=UNIT, default='pieces')
    quantity = models.PositiveIntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_products', default=1)
    
    def __str__(self):
        return self.name
    