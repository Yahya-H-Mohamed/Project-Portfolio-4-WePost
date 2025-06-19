from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('sports', 'Sports'),
    ('entertainment', 'Entertainment'),
    ('education', 'Education'),
    ('technology', 'Technology'),
    ('other', 'Other'),
]

# Create your models here.
class Post(models.Model):
  post_title = models.CharField(max_length=200, unique=True)
  author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts")
  content = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  edited = models.BooleanField(default=False)
  category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')

  def __str__(self):
        return f"Post Title: {self.post_title}, Post Author: {self.author}"
  
  class Meta:
      ordering = ["-created_on"]

class Comment(models.Model):
  original_post = models.ForeignKey(
    Post, on_delete=models.CASCADE, related_name="post_comments")
  author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="comment_author")
  content = models.TextField()
  created_on = models.DateTimeField(auto_now_add=True)
  edited = models.BooleanField(default=False)

  def __str__(self):
        return f"Comment: {self.content}, Comment Author: {self.author}"
  
  class Meta:
      ordering = ["-created_on"]