# Generated by Django 2.2.6 on 2019-10-15 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0037_auto_20191015_1932'),
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
