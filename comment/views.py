from learning_logs.views import article
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import User
from learning_logs.models import Article
from .models import Comment
from .forms import CommentForm

# Create your views here.
def comment_view(request):
    """add a comment to Article 只用管POST，GET由comment_block处理了"""
    target = request.POST.get('target')
    article = Article.objects.get(id=target)

    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.content_object = article
        new_comment.user_belong = request.user
        new_comment.save()
        return HttpResponseRedirect(reverse('learning_logs:article',args=target))


def add_comment_c(request,comment_id):
    """add a comment to Comment"""
    comment = Comment.objects.get(id = comment_id)
    article = Article.objects.get(comment_info=comment)
    target_user = comment.user_belong

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.content_object = comment
            new_comment.user_belong = request.user
            new_comment.save()
            return HttpResponseRedirect(reverse('learning_logs:article',args=(article.id,)))

    context = {
        'target_user':target_user,
        'target_comment':comment,
        'form':form,
    }
    return render(request, 'comment_to_comment.html', context)
    

