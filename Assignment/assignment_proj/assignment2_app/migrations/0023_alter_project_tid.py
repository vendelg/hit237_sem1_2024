# Generated by Django 4.2.13 on 2024-05-28 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment2_app', '0022_delete_requests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tid',
            field=models.IntegerField(max_length=3, primary_key=True, serialize=False),
        ),
    ]
