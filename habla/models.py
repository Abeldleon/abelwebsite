from django.db import models
from django.utils import timezone

class Post(models.Model):

    options = {
        ("draft", "Draft"),
        ("published", "published"),
    }

    title = models.CharField(max_length=200)

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.CharField(max_length=10, choices=options, default="draft")
    
    class Meta:
        ordering = ("-created_at",)
    def __str__(self):
        return self.title


    
# Create your models here.
