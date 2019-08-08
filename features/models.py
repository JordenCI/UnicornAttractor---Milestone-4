from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=75, blank=False)
    desc = models.TextField(max_length=500, blank=False)
    upvotes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)
    
    STATUS_CHOICES = (
        ('To do', 'To do'),
        ('In progress', 'In progress'),
        ('Done', 'Done'),
        ('Cancelled', 'Cancelled')
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='To do'
    )

    def __str__(self):
        return self.name
        
class FeatureComment(models.Model):
    description = models.TextField(max_length=256, blank=False)
    feature = models.ForeignKey(Feature)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.description
