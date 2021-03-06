# Generated by Django 3.0.4 on 2020-05-03 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_entry_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='description',
            field=models.CharField(default='no description', max_length=100, verbose_name='分类描述'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.CharField(default=2, max_length=100, verbose_name='标签描述'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=models.CharField(max_length=50, verbose_name='分类名'),
        ),
    ]
