from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment, CATEGORY_CHOICES
from .form import CommentForm, PostForm


# Create your views here.
class PostList(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CATEGORY_CHOICES
        context['selected_category'] = self.request.GET.get('category', '')
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset.order_by('-created_on')


class MyPosts(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'blog/my_posts.html'
    paginate_by = 5
    context_object_name = 'posts'  

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-created_on')


def create_post(request):
    """
    view to create post
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  
            post.save()
            return redirect('my_posts')
    else:
        form = PostForm()
    
    return render(request,
                  'blog/create_post.html',
                  {'form': form})


def post_detail(request, post_id):
    """
    view to post details
    """
    post = get_object_or_404(Post, id=post_id)
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


def comment_edit(request, post_id, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        post = get_object_or_404(Post, id=post_id)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.edited = True
            comment.save()

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, post_id, comment_id):
    """
    view to delete comment
    """
    post = get_object_or_404(Post, id=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))