# Generated by Django 3.1.5 on 2021-02-05 20:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donatebook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdonation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
