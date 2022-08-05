# Generated by Django 4.0.6 on 2022-08-03 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_merge_0004_alter_blog_image_0007_alter_blog_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='created',
        ),
        migrations.RemoveField(
            model_name='like',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='like',
            name='value',
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.CharField(max_length=1000),
        ),
        migrations.RemoveField(
            model_name='blog',
            name='likes',
        ),
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
