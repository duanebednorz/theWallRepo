# Generated by Django 2.2.4 on 2021-03-03 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theWallApp', '0005_auto_20210303_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='wallMessage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallComments', to='theWallApp.User'),
        ),
    ]
