# Generated by Django 2.2.6 on 2019-10-11 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0024_sweets_counts2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sweets',
            name='counts2',
        ),
    ]
