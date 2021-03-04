# Generated by Django 2.2.4 on 2021-03-03 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theWallApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='users_who_like',
            field=models.ManyToManyField(related_name='likesMessage', to='theWallApp.User'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='users_who_like',
            field=models.ManyToManyField(related_name='likesComment', to='theWallApp.User'),
        ),
    ]
