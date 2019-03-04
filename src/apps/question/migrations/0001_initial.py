# Generated by Django 2.1.7 on 2019-03-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account_hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=256, unique=True, verbose_name='Slug')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='Answer')),
                ('account_hr', models.ManyToManyField(blank=True, related_name='questions', to='account_hr.AccountHr', verbose_name='Questions')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
    ]
