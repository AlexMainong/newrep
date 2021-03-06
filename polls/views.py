from django.shortcuts import render
from .models import Post, Comments, PostStatistic
from django.http import Http404
from django.utils import timezone
from .forms import PostForm, CommentsForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
import json
from django.views.generic import RedirectView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect(reverse('post_details', kwargs={"pk": post.pk}))
    else:
        form = PostForm(instance=post)
    return render(request, 'polls/post_edit.html', {'form': form, 'username': auth.get_user(request).username})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect(reverse('post_details', kwargs={"pk": post.pk}))
    else:
        form = PostForm()
    return render(request, 'polls/post_edit.html', {'form': form})
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'polls/post_list.html', { 'posts': posts, 'username': auth.get_user(request).username})
def post_details(request, pk, *args, **kwargs):
    comment_form = CommentsForm
    comments = Comments.objects.filter(post_comment=pk)
    post = get_object_or_404(Post, id=pk)
    context = {}
    obj, created = PostStatistic.objects.get_or_create(
        defaults={
            "post": post, "date": timezone.now()
        },
        post=post
    )
    obj.views += 1
    obj.save(update_fields=['views'])
    return render(request, 'polls/post_details.html',  {'post': post, 'username': auth.get_user(request).username, 'comment_form': comment_form, 'comments': comments})

@login_required(login_url='/auth/login/')
def new_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_comment = Post.objects.get(id=post.pk)
            comment.comment_from = auth.get_user(request)
            comment.comment_date = timezone.now()
            form.save()
    return redirect(reverse('post_details', kwargs={"pk": post.pk}))

def add_like(request, pk):
    post = get_object_or_404(Post, pk=pk )
    print("slug")
    user = request.user
    if user.is_authenticated():
        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)
    return redirect("/")

class PostLikeAPIToggle(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None, pk=None):
        obj = get_object_or_404(Post, pk=pk)
        user = self.request.user
        updated = False
        liked = False
        if user.is_authenticated():
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)
            updated = True
        data = {
            "updated": updated,
            "liked": liked
        }
        return Response(data)


# Create your views here.
