# Generated by Django 2.0.3 on 2018-06-23 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180623_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content1',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='photo1',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='photo2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='photo3',
        ),
    ]
