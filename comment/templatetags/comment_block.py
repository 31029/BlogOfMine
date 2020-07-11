from django import template

from comment.forms import CommentForm
from comment.models import Comment

register = template.Library()

@register.inclusion_tag('block.html')
def comment_block(target, user):
    return {
        'user':user,
        'target':target,
        'comment_form':CommentForm,
        'comment_list':Comment.get_comments(target),
    }