# Generated by Django 3.0.5 on 2020-04-30 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200429_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='icon',
            field=models.ImageField(blank=True, upload_to='uploads/images/'),
        ),
    ]
