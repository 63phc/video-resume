# Generated by Django 2.1.5 on 2019-03-11 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_hr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounthr',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hrs', to=settings.AUTH_USER_MODEL, verbose_name='hrs'),
        ),
    ]
