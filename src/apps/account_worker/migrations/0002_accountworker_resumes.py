# Generated by Django 2.1.5 on 2019-02-11 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
        ('account_worker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountworker',
            name='resumes',
            field=models.ManyToManyField(to='resume.Resume'),
        ),
    ]
