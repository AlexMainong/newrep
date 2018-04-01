from django.db.models import Sum
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    title = models.CharField(max_length=200, verbose_name=u"Заголовок")
    text = RichTextUploadingField(('Статья'))
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    likes = models.ManyToManyField('auth.User', blank=True, related_name='post_like')


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class Comments(models.Model):
    text = models.CharField(max_length=200, verbose_name=u"Ваш комментарий")
    post_comment = models.ForeignKey(Post, null=True, on_delete=models.DO_NOTHING)
    comment_date = models.DateTimeField(null=True)
    comment_from = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING,)


class PostStatistic(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING,)
    date = models.DateField('Дата', default=timezone.now)
    views = models.IntegerField('Просмотры', default=0)

    def __str__(self):
        return self.post.title


class PostStatisticAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date', 'views')
    search_fields = ('__str__', )
