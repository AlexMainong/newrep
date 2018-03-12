from django.shortcuts import render
from .models import Post, Comments
from django.http import Http404
from django.utils import timezone
from .forms import PostForm, CommentsForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    return render(request, 'polls/post_edit.html', {'form': form})
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
def post_details(request, pk):
    comment_form = CommentsForm
    comments = Comments.objects.filter(post_comment=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'polls/post_details.html', {'post': post, 'username': auth.get_user(request).username, 'comment_form': comment_form, 'comments': comments})

def new_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_comment = Post.objects.get(id=post.pk)
            form.save()
    return redirect(reverse('post_details', kwargs={"pk": post.pk}))


# Create your views here.
