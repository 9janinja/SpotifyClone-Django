# Generated by Django 2.2.6 on 2019-10-21 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='song_file',
            new_name='profile_pic',
        ),
    ]