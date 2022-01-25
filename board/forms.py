from django import forms
from django_summernote.widgets import SummernoteWidget

from board.models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(),
        }
