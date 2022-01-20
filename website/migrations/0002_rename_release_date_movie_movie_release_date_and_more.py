# Generated by Django 4.0 on 2022-01-06 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='release_date',
            new_name='movie_release_date',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='title',
            new_name='movie_title',
        ),
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.FloatField(),
        ),
    ]
