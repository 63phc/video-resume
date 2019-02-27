# Generated by Django 2.1.5 on 2019-02-27 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account_hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Name')),
                ('slug', models.SlugField(max_length=256, unique=True, verbose_name='Slug')),
                ('is_activated', models.BooleanField(default=False, verbose_name='Activated')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('slug', models.SlugField(max_length=256, unique=True, verbose_name='Slug')),
                ('is_activated', models.BooleanField(default=False, verbose_name='Activated')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('account_hr', models.ManyToManyField(related_name='vacancies', to='account_hr.AccountHr', verbose_name='HRs')),
                ('tags', models.ManyToManyField(related_name='vacancies', to='vacancy.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Vacancy',
                'verbose_name_plural': 'Vacancies',
            },
        ),
    ]
