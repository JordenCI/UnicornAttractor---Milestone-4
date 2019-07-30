from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Bug(models.Model):
    name = models.CharField(max_length=75)
    desc = models.TextField(max_length=500)
    upvotes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='created_by')

    def __str__(self):
        return self.name
        
class BugComment(models.Model):
    description = models.TextField()
    bug = models.ForeignKey(Bug)
    author = models.ForeignKey(User)
    
    def __str__(self):
        return self.description