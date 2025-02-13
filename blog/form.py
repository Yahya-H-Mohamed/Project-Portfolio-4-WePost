from .models import Post, Comment
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'content']
    
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
    
    content = forms.CharField(
        label='',  # Remove label
        widget=forms.Textarea(attrs={
            'placeholder': 'Write your comment here...',  # Placeholder
            'rows': 3,
        })
    )


