from django.db import models
from martor.models import MartorField

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = MartorField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Meta:
    ordering = ['created']