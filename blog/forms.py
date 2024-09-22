from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        from .models import Comment
        model = Comment
        fields = ['name', 'email', 'comment_text', 'parent']
        widgets = {
            'parent': forms.HiddenInput(),  # This will be filled when replying to a comment
        }