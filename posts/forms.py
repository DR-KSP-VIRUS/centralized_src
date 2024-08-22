from django import forms

from . import models as mdl 


class BlogForm(forms.ModelForm):
    class Meta:
        model = mdl.Post
        fields = ['title','content',]

        widgets = {
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'e.g FIRST SCR GA MEETING',
                'required': True, 'autofocus':True
            }),
            'content':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'e.g Important and Other things',
                'required':True
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = mdl.PostComment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={
                'class':'form-control',
                'required':True, 'autofocus':True,
                'placeholder':'Type your comment here ...',
                'rows':2,
            })
        }
