# Generated by Django 2.0.13 on 2019-04-18 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('level_system', '0003_auto_20190418_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlevel',
            name='xp_threshold',
            field=models.IntegerField(default=100),
        ),
    ]
