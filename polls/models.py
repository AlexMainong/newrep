
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
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
    text = models.TextField(max_length=140)
    post_comment = models.ForeignKey(Post, null=True, on_delete=models.DO_NOTHING)
    comment_date = models.DateTimeField(null=True)
    comment_from = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING,)
class PostStatistic(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING,)                    # внешний ключ на статью
    date = models.DateField('Дата', default=timezone.now)   # дата
    views = models.IntegerField('Просмотры', default=0)     # количество просмотров в эту дату

    def __str__(self):
        return self.post.title


class PostStatisticAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date', 'views')  # отображаемые поля в админке
    search_fields = ('__str__', )
