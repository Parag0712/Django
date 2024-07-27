from django.db import models
from django.utils import timezone
# Create your models here.
class ChaiVarity(models.Model):
    TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),  # Fixed typo from 'GIGER' to 'GINGER'
        ('PL', 'PLAIN'),   # Fixed typo from 'PLAN' to 'PLAIN'
        ('EL', 'ELACHI'),  # Fixed typo from 'EL:' to 'EL'
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='imagechai/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=TYPE_CHOICE, default='ML')
    description = models.TextField(default='')
    
    def __str__(self):
        return self.name

class Notes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name