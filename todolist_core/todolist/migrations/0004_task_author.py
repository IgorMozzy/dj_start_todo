# Generated by Django 5.0.6 on 2024-07-03 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='author',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
