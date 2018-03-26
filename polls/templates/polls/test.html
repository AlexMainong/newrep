from django import template
from django.db.models import Sum
from django.utils import timezone
from django.conf import settings
from django.shortcuts import render
from polls.models import PostStatistic

register = template.Library()


@register.assignment_tag
def get_popular():
    context = {}
    popular = PostStatistic.objects.filter(
        date__range=[timezone.now() - timezone.timedelta(7), timezone.now()]
    ).values(
        'post_id', 'post__title'
    ).annotate(

        view=Sum('views')
    ).order_by(
        '-views')[:5]
    return popular
