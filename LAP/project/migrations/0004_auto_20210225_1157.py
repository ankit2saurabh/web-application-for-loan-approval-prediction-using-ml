# Generated by Django 3.1.5 on 2021-02-25 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20210222_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='fb',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='project',
            name='tw',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='project',
            name='yt',
            field=models.TextField(default='-'),
        ),
    ]
