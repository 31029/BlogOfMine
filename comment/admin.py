from django.contrib import admin
from comment.models import Comment

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_belong', 'content_object','created_time','content',)
