# Generated by Django 4.2.13 on 2024-05-27 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment2_app', '0008_accounts_is_loggedin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='is_loggedin',
        ),
    ]
