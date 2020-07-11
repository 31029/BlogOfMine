# Generated by Django 3.0.4 on 2020-05-03 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0006_auto_20200503_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.CharField(default='暂未填写内容', max_length=5000, verbose_name='文章内容'),
        ),
        migrations.AlterField(
            model_name='article',
            name='topic',
            field=models.CharField(default='无标题', max_length=40, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='description',
            field=models.CharField(default='无描述', max_length=100, verbose_name='分类描述'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=models.CharField(default='无分类', max_length=50, verbose_name='分类名'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.CharField(default='暂无表述', max_length=100, verbose_name='标签描述'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='text',
            field=models.CharField(default='暂无标签', max_length=40, verbose_name='标签'),
        ),
    ]