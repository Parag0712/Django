from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
# ChaiVarity
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

# Notes Model
class Notes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name

# One to Many
class ChaiReviw(models.Model):
    chai = models.ForeignKey(ChaiVarity,on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[    
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    comment = models.TextField()
    date_add = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.user.username} review for {self.chai.name}" 

# Many to Many
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varity = models.ManyToManyField(ChaiVarity,related_name='stores')
    def __str__(self):
        return self.name

# one to one
class Certificate(models.Model):
    chai = models.OneToOneField(ChaiVarity,on_delete=models.CASCADE,related_name="certificate")
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    validate_date = models.DateTimeField()

    def __str__(self):
        return f"Certificate for {self.name}"
