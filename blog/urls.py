from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('my_posts/', views.MyPosts.as_view(), name='my_posts'),
    path('create_post/', views.create_post, name='create_post'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<int:post_id>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]