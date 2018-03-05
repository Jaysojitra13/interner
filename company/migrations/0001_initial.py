# Generated by Django 2.0.1 on 2018-02-06 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('intern', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='company_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hr_fname', models.CharField(max_length=20)),
                ('hr_lname', models.CharField(max_length=20)),
                ('hr_email', models.EmailField(max_length=254)),
                ('website_url', models.URLField()),
                ('location', models.CharField(max_length=50)),
                ('contact_numbrt', models.BigIntegerField()),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='company.CompanyProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PostDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=20)),
                ('technology', models.CharField(max_length=20)),
                ('numberof_interns', models.IntegerField()),
                ('time_duration', models.IntegerField()),
                ('stipend', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('apply_by', models.DateTimeField()),
                ('typeof_internship', models.CharField(max_length=20)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.CompanyProfile')),
            ],
        ),
        migrations.CreateModel(
            name='UserPostConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=25)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.CompanyProfile')),
                ('internprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intern.InternProfile')),
                ('postdetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.PostDetails')),
            ],
        ),
    ]
