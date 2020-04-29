from django.contrib import admin

# Register your models here.
from learning_logs.models import Article ,Entry, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ('text',)
    list_display = ('text',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('text', 'tag', 'entry')
    list_display = ['text', 'date_added',  'entry']


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    fields = ('text',)
