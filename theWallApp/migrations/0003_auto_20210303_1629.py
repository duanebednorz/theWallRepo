# Generated by Django 2.2.4 on 2021-03-03 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theWallApp', '0002_auto_20210303_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='users_who_dislike',
            field=models.ManyToManyField(related_name='dislikesComment', to='theWallApp.User'),
        ),
        migrations.AddField(
            model_name='message',
            name='users_who_dislike',
            field=models.ManyToManyField(related_name='dislikesMessage', to='theWallApp.User'),
        ),
    ]
