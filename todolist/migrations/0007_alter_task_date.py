# Generated by Django 4.1 on 2022-09-28 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_alter_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
