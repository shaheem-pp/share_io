# Generated by Django 4.0.6 on 2022-07-31 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='media/dummy-image.jpeg', upload_to=''),
            preserve_default=False,
        ),
    ]