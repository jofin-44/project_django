# Generated by Django 4.2.7 on 2024-02-07 19:06

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New_Reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=200, verbose_name=django.contrib.auth.models.User)),
                ('email', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('c_password', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
