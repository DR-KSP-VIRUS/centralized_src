from django.db import models
from django.contrib.auth import get_user_model
from django_ckeditor_5.fields import CKEditor5Field


User = get_user_model()

# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts') 
    title = models.CharField(blank=True, null=True, max_length=255)
    text = CKEditor5Field(null=True, blank=False, config_name='extends')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    show_from = models.DateTimeField(null=True)
    show_to = models.DateTimeField(null=True)


    def __str__(self) -> str:
        return self.title
    
class PostComment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user_comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def _str__(self):
        return self.comment[:50]
    
class Complain(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_complain')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} complains"
    
class FeedBack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_feedback")
    complain = models.ForeignKey(Complain, on_delete=models.CASCADE, related_name='complain_feedback')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} {self.complain} Feedback"