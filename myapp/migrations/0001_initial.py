# Generated by Django 3.2 on 2021-04-20 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('ID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('albums', models.URLField()),
                ('tracks', models.URLField()),
                ('myself', models.URLField()),
            ],
        ),
    ]
