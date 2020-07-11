from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User, ContentType

import learning_logs.models as amodel


# Create your models here.
class Comment(models.Model):
    """Comment aimed at: Discussion, Article and User's comment"""
    user_belong = models.ForeignKey(to=User, on_delete=models.CASCADE)
    content = models.CharField(max_length=100, verbose_name="评论内容")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")

    #GenericForeikey的设计
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    #实际操作中用到的
    content_object = GenericForeignKey()

    class Meta:
        verbose_name = verbose_name_plural = "评论"
    def __str__(self):
        return self.content[:50]
    
    @classmethod
    def get_comments(cls, target):
        article = amodel.Article.objects.get(id=target)
        comments = article.comment_info.all()
        return comments

    def get_inner_comments(self):
        test_model_ct = ContentType.objects.get_for_model(Comment)
        inner_comments = Comment.objects.filter(content_type=test_model_ct, object_id=self.id)
        for comment in inner_comments:
            if comment.get_inner_comments():
                inner_comments = inner_comments + comment.get_inner_comments()

        return inner_comments
