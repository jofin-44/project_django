# Generated by Django 4.2.7 on 2024-02-06 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.IntegerField()),
                ('message', models.TextField(max_length=250)),
            ],
        ),
    ]
