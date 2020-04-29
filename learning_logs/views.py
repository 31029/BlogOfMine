from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Article, Entry
from .forms import ArticleForm, EntryForm

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

@login_required
def articles(request):
    """Show all articles."""
    articles = Article.objects.filter(owner=request.user).order_by('date_added')
    context = {'articles': articles}
    return render(request, 'learning_logs/articles.html', context)

@login_required
def article(request, article_id):
    """Show a single article, and its entry."""
    article = Article.objects.get(id=article_id)
    # Make sure the article belongs to the current user.
    if article.owner != request.user:
        raise Http404
        
    entry= article.entry
    context = {'article': article, 'entry': entry}
    return render(request, 'learning_logs/article.html', context)

@login_required
def new_article(request):
    """Add a new article."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ArticleForm()
    else:
        # POST data submitted; process data.
        form = ArticleForm(request.POST)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.owner = request.user
            new_article.save()
            return HttpResponseRedirect(reverse('learning_logs:articles'))

    context = {'form': form}
    return render(request, 'learning_logs/new_article.html', context)

@login_required
def new_entry(request, article_id):
    """Add a new entry for a particular article."""
    article = Article.objects.get(id=article_id)
    if article.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()        
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.article = article
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:article',
                                        args=[article_id]))
    
    context = {'article': article, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    article = entry.article_set().all()
    #if article.owner != request.user:
    #   raise Http404
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:article',
                                        args=[article.id]))
    
    context = {'entry': entry, 'article': article, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
