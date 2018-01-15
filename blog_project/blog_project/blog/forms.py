from django import forms
from .models import Post, Comment

class PostForm (forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        # Adding widgets
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            # giving the form a textarea attribute. It will get from 3 CSS classes:  ediitable, medium-editor-textarea (connects to Medium text area), postcontent (own class)
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }


class CommentForm (forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        # Adding widgets
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
