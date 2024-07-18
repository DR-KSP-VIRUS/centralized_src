from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts') 
    title = models.CharField(blank=True, null=True, max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    show_from = models.DateTimeField(null=True)
    show_to = models.DateTimeField(null=True)


    def __str__(self) -> str:
        return self.title