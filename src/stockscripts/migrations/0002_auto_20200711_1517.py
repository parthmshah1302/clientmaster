# Generated by Django 2.1.5 on 2020-07-11 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockscripts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='Script_code',
            new_name='Script',
        ),
    ]
