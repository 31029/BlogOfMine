from django import forms
from .models import Article, Entry


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['topic', 'tag', 'entry', 'text',]
        labels = {'text': ''}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80}),
        }

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'description']
        labels = {'text': '分类', 'decsription':'描述'}
        widgets = {}
