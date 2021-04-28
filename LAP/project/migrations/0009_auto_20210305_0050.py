# Generated by Django 3.1.6 on 2021-03-04 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_services'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name_plural': 'Project'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name_plural': 'Service'},
        ),
        migrations.RenameField(
            model_name='services',
            old_name='about',
            new_name='buttonlink',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='services',
            name='fb',
        ),
        migrations.RemoveField(
            model_name='services',
            name='gml',
        ),
        migrations.RemoveField(
            model_name='services',
            name='insta',
        ),
        migrations.RemoveField(
            model_name='services',
            name='linkden',
        ),
        migrations.RemoveField(
            model_name='services',
            name='set_name',
        ),
        migrations.RemoveField(
            model_name='services',
            name='tw',
        ),
        migrations.AddField(
            model_name='services',
            name='iconclass',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='services',
            name='serviceBody',
            field=models.CharField(default='-', max_length=50),
        ),
    ]