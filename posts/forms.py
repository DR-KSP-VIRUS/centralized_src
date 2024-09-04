from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from . import models as mdl 


class BlogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields["text"].required = False

    class Meta:
        model = mdl.Post
        fields = ['title','text',]

        widgets = {
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'e.g FIRST SCR GA MEETING',
                'required': True, 'autofocus':True
            }),
            'text':CKEditor5Widget(),
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
