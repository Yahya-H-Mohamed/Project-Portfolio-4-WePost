from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('post_title', 'author', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['post_title', 'content']  
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)