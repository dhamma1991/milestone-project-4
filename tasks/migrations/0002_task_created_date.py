# Generated by Django 2.0.13 on 2019-04-08 19:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 8, 19, 22, 7, 42751, tzinfo=utc), editable=False),
        ),
    ]
