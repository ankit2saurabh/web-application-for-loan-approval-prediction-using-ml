# Generated by Django 3.1.5 on 2021-03-04 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20210225_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('fb', models.CharField(default='-', max_length=100)),
                ('tw', models.CharField(default='-', max_length=100)),
                ('insta', models.CharField(default='-', max_length=100)),
                ('linkden', models.CharField(default='-', max_length=100)),
                ('gml', models.CharField(default='-', max_length=100)),
                ('set_name', models.CharField(default='-', max_length=20)),
                ('about', models.TextField()),
            ],
        ),
    ]