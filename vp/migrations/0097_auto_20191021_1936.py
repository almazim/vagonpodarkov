# Generated by Django 2.2.6 on 2019-10-21 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0096_auto_20191021_1931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classic',
            old_name='type_box',
            new_name='typebox',
        ),
        migrations.RenameField(
            model_name='premium',
            old_name='type_box',
            new_name='typebox',
        ),
    ]
