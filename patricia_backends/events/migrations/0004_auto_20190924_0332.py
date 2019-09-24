# Generated by Django 2.2.4 on 2019-09-24 03:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190922_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('Free Ticket', 'Free Ticket'), ('Ticket With Fee', 'Ticket With Fee')], default='Free Ticket', max_length=100),
        ),
        migrations.AlterField(
            model_name='new',
            name='detail',
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='new',
            name='published_date',
            field=models.DateField(default=datetime.date(2019, 9, 24)),
        ),
    ]