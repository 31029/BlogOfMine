# Generated by Django 3.0.4 on 2020-04-29 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_article_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='topic',
            field=models.CharField(default='NULL', max_length=40, verbose_name='标题'),
            preserve_default=False,
        ),
    ]
