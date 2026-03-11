from django.db import models
from apps.core.models import Product

class Comment(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.URLField(blank=True, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name