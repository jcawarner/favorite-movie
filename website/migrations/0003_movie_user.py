# Generated by Django 4.0 on 2022-01-06 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('website', '0002_rename_release_date_movie_movie_release_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]