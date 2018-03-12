from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class Comments(models.Model):
    text = models.TextField()
    post_comment = models.ForeignKey(Post, null=True)
    comment_date = models.DateTimeField(null=True)
    comment_from = models.ForeignKey(User, null=True)
