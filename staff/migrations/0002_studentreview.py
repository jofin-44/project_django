# Generated by Django 4.2.7 on 2024-02-07 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentreview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('event', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=250)),
            ],
        ),
    ]