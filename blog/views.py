from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .form import CommentForm

# Create your views here.
class PostList(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5

def post_detail(request, slug):
    queryset = Post.objects.all()
    post = get_object_or_404(Post, id=slug)
    comments = post.post_comments.all().order_by("-created_on")

    comment_form = CommentForm()

    if request.method == "POST":
      comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.original_post = post
        comment.author = request.user
        comment.save()

    return render(
        request,
        "blog/post_detail.html",
        {"post": post,
         "comments": comments,
         "comment_form": comment_form,},
    )