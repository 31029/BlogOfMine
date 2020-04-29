from django import forms
from .models import Article, Entry

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['text', 'tag', 'entry']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
