# Generated by Django 2.0.13 on 2019-04-20 02:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_profile_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_login',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
