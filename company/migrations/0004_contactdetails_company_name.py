# Generated by Django 2.0.1 on 2018-02-09 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20180208_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdetails',
            name='company_name',
            field=models.CharField(default=' ', max_length=30),
            preserve_default=False,
        ),
    ]
