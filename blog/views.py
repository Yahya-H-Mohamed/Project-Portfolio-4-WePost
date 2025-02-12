from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5

def post_detail(request, slug):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, id=slug)
    post = get_object_or_404(Post, id=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )