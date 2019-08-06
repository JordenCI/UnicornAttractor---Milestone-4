from django import forms
from .models import ForumPost, ForumComment

class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ('name', 'desc')
        
class ForumCommentForm(forms.ModelForm):
    class Meta:
        model = ForumComment
        fields=('description',)