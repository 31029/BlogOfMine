from django.contrib import admin

# Register your models here.
from learning_logs.models import Article ,Entry, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ('text','description',)
    list_display = ('text', 'description',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('text', 'tag', 'entry')
    list_display = ['text', 'date_added',  'entry']


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    fields = ('text', 'owner')
    list_display = ['text', 'date_added',  'owner']