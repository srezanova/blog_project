from .models import Comment, Post
from django import forms
from django.forms import widgets


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea form-control'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea form-control'})
        }