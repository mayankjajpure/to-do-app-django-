# Generated by Django 3.2 on 2021-05-01 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='decs',
            new_name='taskDesc',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='taskTitle',
        ),
    ]
