# Generated by Django 2.2.4 on 2019-08-27 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botusers', '0002_botuser_registered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='botuser',
            name='registered',
        ),
    ]