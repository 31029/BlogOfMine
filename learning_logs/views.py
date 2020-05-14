from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

from learning_log.decorators import is_31029
from .models import Article, Entry
from .forms import ArticleForm, EntryForm

def index(request):
    """The home page for Learning Log."""
    #展示最新最热文章和分类
    if request.user.is_authenticated:
        #owner_id = request.user.id
        owner_id = 1
    else:
        owner_id = 1
    top_articles = Article.objects.filter(owner_id=owner_id)
    top_entries = User.objects.get(id=owner_id).entry_set.all()
    #统计特定用户下entry的个数
    numbers = Entry.objects.filter(owner_id=1).count()
    context = {
        'top_articles': top_articles[:6],
        'top_entries': top_entries[:4],
        'numbers': numbers,
    }  
    return render(request, 'learning_logs/index.html', context)


def articles(request):
    """Show all articles."""
    user = 1 #request.user
    articles = Article.objects.filter(owner=user).order_by('date_added')

    context = {'articles': articles}
    return render(request, 'learning_logs/articles.html', context)


def article(request, article_id):
    """Show a single article, and its entry."""
    article = Article.objects.get(id=article_id)
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


def entry(request, entry_id):
    """show a entry and it's articles"""
    entry = Entry.objects.get(id=entry_id)
    articles = entry.article_set.all()

    context = {'entry':entry, 'articles':articles}
    return render(request, 'learning_logs/entry.html', context) 


def entries(request):
    """show all entries of a user."""
    user = 1 #request.user.id
    entries = User.objects.get(id=user).entry_set.all()

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()        
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:entries'))
    
    context = {'entries': entries, 'form': form}
    return render(request, 'learning_logs/entries.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    articles = Article.objects.filter(entry_id=entry_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:articles'))
    
    context = {'entry': entry, 'articles': articles, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


@login_required
def edit_article(request, article_id):
    """edit an existing article"""
    article = Article.objects.get(id=article_id)
    entry = article.entry

    if request.method != 'POST':
    # Initial request; pre-fill form with the current entry.
        form = ArticleForm(instance=article)
    else:
        # POST data submitted; process data.
        form = ArticleForm(instance=article, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:articles'))
    
    context = {'entry': entry, 'article': article, 'form': form}
    return render(request, 'learning_logs/edit_article.html', context)
    

def searchview(request):
    """searching function"""
    keyword = request.GET.get('keyword')
    #articles = article.tag.filter(text__icontains=keyword)
    if keyword is None:
        articles = Article.objects.filter(owner=1).order_by('date_added')
    else:
        articles = Article.objects.filter(Q(topic__icontains=keyword) | Q(tag__text__icontains=keyword)).order_by('date_added')
    articles = articles.distinct()
    context = {
        'articles':articles,
    }
    return render(request, 'learning_logs/articles.html', context)