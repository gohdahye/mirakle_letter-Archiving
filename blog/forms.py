from django.forms import DateInput
from django_summernote.widgets import SummernoteWidget

from .models import Comment, Post
from django import forms

from .widgets import CounterTextInput


class PostForm(forms.ModelForm):
    title = forms.CharField(
        label="제목",
        required=True,
    )

    hook_text = forms.CharField(
        label="소제목",
        required=True,
        widget=CounterTextInput,
    )

    content = forms.CharField(
        label="내용",
        required=True,
        widget=SummernoteWidget(),
    )

    head_image = forms.FileField(
        label="메인 이미지",
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'multiple': True,
            'class': 'file-upload-native',
            'accept': '.jpeg,.png,.gif'
        })
    )

    pub_date = forms.DateField(
        label="발행일",
        required=True,
        widget=DateInput(attrs={
            'type':'date',
            'style':'max-width:250px'
        })
    )

    class Meta:
        model = Post
        fields = ['title', 'hook_text', 'content', 'head_image', 'pub_date',  'category']



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content', ]
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 15}),
        }
