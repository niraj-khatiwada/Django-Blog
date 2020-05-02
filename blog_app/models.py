from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BlogPostModel(models.Model):
    post_title = models.CharField(max_length=255)
    post_text = models.TextField()
    posted_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post_title}, {self.author}'

    class Meta:
        db_table = "blog"