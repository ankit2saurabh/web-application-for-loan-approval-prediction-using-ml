# Generated by Django 3.1.7 on 2021-03-23 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_remove_eligblity_fathername'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='subjeect',
            new_name='subject',
        ),
    ]