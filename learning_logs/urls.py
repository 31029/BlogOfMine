"""Defines url patterns for learning_logs."""

from django.conf.urls import url

from . import views

app_name='learning_logs'
urlpatterns = [
    # Home page.
    url(r'^$', views.index, name='index'),
    
    # Show all articles.
    url(r'^articles/$', views.articles, name='articles'),
    
    # Detail page for a single article.
    url(r'^articles/(?P<article_id>\d+)/$', views.article, name='article'),
    
    # Page for adding a new article.
    url(r'^new_article/$', views.new_article, name='new_article'),
    
    # Page for adding a new entry.
    url(r'^new_entry/(?P<article_id>\d+)/$', views.new_entry, name='new_entry'),
    
    # Page for editing an entry.
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
        name='edit_entry'),
]
