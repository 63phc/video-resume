# Generated by Django 2.1.5 on 2019-02-25 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0003_adding_verbose_names_to_the_model_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at'),
        ),
        migrations.AddField(
            model_name='tag',
            name='is_activated',
            field=models.BooleanField(default=False, verbose_name='Activated'),
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, max_length=256, null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='tag',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Updated_at'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created at'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='is_activated',
            field=models.BooleanField(default=False, verbose_name='Activated'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='slug',
            field=models.SlugField(blank=True, max_length=256, null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Updated_at'),
        ),
    ]
