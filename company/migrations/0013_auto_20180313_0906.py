# Generated by Django 2.0.1 on 2018-03-13 09:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0012_auto_20180313_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpostconnection',
            name='applied_date',
            field=models.DateField(default=datetime.date(2018, 3, 13)),
        ),
        migrations.AlterField(
            model_name='userpostconnection',
            name='stausupdate_date',
            field=models.DateField(default=datetime.date(2018, 3, 13)),
        ),
    ]
