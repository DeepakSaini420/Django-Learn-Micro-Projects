# Generated by Django 4.2.4 on 2023-08-17 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('url', models.URLField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('clicks', models.IntegerField(default=0)),
            ],
        ),
    ]
