# Generated by Django 2.2.6 on 2019-10-15 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0041_auto_20191015_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classic',
            old_name='image',
            new_name='classic',
        ),
        migrations.RenameField(
            model_name='premium',
            old_name='image',
            new_name='premium',
        ),
    ]
