# Generated by Django 2.0.1 on 2018-03-14 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0016_postdetails_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpostconnection',
            old_name='stausupdate_date',
            new_name='statusupdate_date',
        ),
        migrations.AlterField(
            model_name='messages',
            name='message_date',
            field=models.DateField(default=datetime.date(2018, 3, 14)),
        ),
    ]
