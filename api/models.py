from django.db import models

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
    
    def __str__(self):
        return self.name
    