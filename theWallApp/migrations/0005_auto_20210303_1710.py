# Generated by Django 2.2.4 on 2021-03-03 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theWallApp', '0004_auto_20210303_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='users_who_dislike',
            field=models.ManyToManyField(related_name='dislikesComment', to='theWallApp.User'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='users_who_like',
            field=models.ManyToManyField(related_name='likesComment', to='theWallApp.User'),
        ),
        migrations.AlterField(
            model_name='message',
            name='users_who_dislike',
            field=models.ManyToManyField(related_name='dislikesMessage', to='theWallApp.User'),
        ),
        migrations.AlterField(
            model_name='message',
            name='users_who_like',
            field=models.ManyToManyField(related_name='likesMessage', to='theWallApp.User'),
        ),
    ]
