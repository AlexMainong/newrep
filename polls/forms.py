from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Post, Comments

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
           'description': CKEditorUploadingWidget()
        }
class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('text',)
