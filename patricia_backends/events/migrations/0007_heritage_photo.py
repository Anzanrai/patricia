# Generated by Django 2.2.4 on 2019-09-24 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_heritage'),
    ]

    operations = [
        migrations.AddField(
            model_name='heritage',
            name='photo',
            field=models.FileField(blank=True, null=True, storage='/media', upload_to=''),
        ),
    ]