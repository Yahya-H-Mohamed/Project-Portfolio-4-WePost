from .models import Comment
from django import forms


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


