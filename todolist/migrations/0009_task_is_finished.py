# Generated by Django 4.1 on 2022-09-28 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0008_alter_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_finished',
            field=models.TextField(default='False'),
        ),
    ]