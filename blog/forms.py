from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['username', 'comment_text']
        labels = {
            "username": "Your Name",
            "comment_text": "Your Comment",
        }
