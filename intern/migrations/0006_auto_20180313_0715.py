# Generated by Django 2.0.1 on 2018-03-13 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intern', '0005_auto_20180313_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_company',
            field=models.BooleanField(default=False),
        ),
    ]