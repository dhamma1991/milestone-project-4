# Generated by Django 2.0.13 on 2019-04-16 17:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0018_auto_20190416_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 16, 17, 1, 37, 802828, tzinfo=utc), editable=False),
        ),
    ]
