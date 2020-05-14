from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    """Some pecific details about the article"""
    text = models.CharField(verbose_name="标签", max_length=40, default="暂无标签")
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.CharField(verbose_name="标签描述", max_length=100, default="暂无表述")

    class Meta:
        verbose_name = verbose_name_plural = "标签"

    def __str__(self):
        return self.text


class Entry(models.Model):
    """Something specific learned about a article."""
    text = models.CharField(verbose_name="分类名", max_length=50, default='无分类')
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(verbose_name="分类描述", max_length=100, default="无描述")

    class Meta:
        verbose_name_plural = '分类'
 
    def __str__(self):
        """Return a string representation of the model."""
        return self.text[:50] + "..."


class Article(models.Model):
    """The core of BLOGOFMINE"""
    topic = models.CharField(verbose_name="标题", max_length=40, default="无标题")
    text = models.CharField(verbose_name="文章内容", max_length=5000, default="暂未填写内容")
    date_added = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(to=Tag, related_name='Tag_Topic')
    entry = models.ForeignKey(to=Entry, on_delete=models.CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)


    class Meta:
        verbose_name = verbose_name_plural = "博文"

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
