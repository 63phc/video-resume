# Generated by Django 2.1.5 on 2019-02-11 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_edu', models.CharField(max_length=50, verbose_name='Period education')),
                ('name_institution', models.CharField(max_length=100, verbose_name='Name of institution')),
                ('faculty', models.CharField(max_length=100, verbose_name='Faculty')),
                ('form_study', models.CharField(max_length=30, verbose_name='Form of study')),
            ],
            options={
                'verbose_name': 'education',
                'verbose_name_plural': 'educations',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_work', models.CharField(max_length=50, verbose_name='Period of work')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
                ('name_company', models.CharField(max_length=100, verbose_name='Company name')),
            ],
            options={
                'verbose_name': 'job',
                'verbose_name_plural': 'jobs',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_skills', models.CharField(max_length=200, verbose_name='Other skills')),
                ('hobbies', models.CharField(max_length=200, verbose_name='Hobbies')),
                ('about', models.CharField(max_length=400, verbose_name='About')),
                ('educations', models.ManyToManyField(to='resume.Education')),
                ('jobs', models.ManyToManyField(to='resume.Job')),
            ],
            options={
                'verbose_name': 'resume',
                'verbose_name_plural': 'resumes',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'skill',
                'verbose_name_plural': 'skills',
            },
        ),
        migrations.AddField(
            model_name='resume',
            name='skills',
            field=models.ManyToManyField(to='resume.Skill'),
        ),
    ]
