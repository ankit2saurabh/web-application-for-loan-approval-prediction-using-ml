# Generated by Django 3.1.7 on 2021-03-23 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0017_auto_20210323_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eligblity',
            name='fathername',
        ),
    ]
