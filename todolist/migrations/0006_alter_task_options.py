# Generated by Django 5.0.6 on 2024-07-19 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_tag_remove_task_tags_task_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
    ]
