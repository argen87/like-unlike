# Generated by Django 3.2.4 on 2021-06-07 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_api', '0003_auto_20210606_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blog_post', to='social_api.User'),
        ),
    ]
