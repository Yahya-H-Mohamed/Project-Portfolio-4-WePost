from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('my_posts/', views.MyPosts.as_view(), name='my_posts'),
    path('create_post/', views.create_post, name='create_post'),
    path('<int:slug>/', views.post_detail, name='post_detail'),
    path('<int:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<int:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]