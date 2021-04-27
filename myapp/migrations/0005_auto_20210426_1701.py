# Generated by Django 3.2 on 2021-04-26 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_album_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.artist'),
        ),
        migrations.AlterField(
            model_name='track',
            name='album_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.album'),
        ),
    ]
