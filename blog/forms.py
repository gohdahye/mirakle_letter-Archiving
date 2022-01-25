from django_summernote.widgets import SummernoteWidget

from .models import Comment, Post
from django import forms


class PostForm(forms.ModelForm):
    title = forms.CharField(
        label="제목",
        required=True,
    )

    hook_text = forms.CharField(
        label="소제목",
        required=True,
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

    file_upload = forms.FileField(
        label="첨부파일",
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'multiple': True,
            'class': 'file-upload-native',
            'accept': '.csv,.xlsx'
        })
    )

    class Meta:
        model = Post
        fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content', ]