# Generated by Django 2.2.6 on 2019-10-11 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0021_auto_20191011_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='sweets',
            name='slug',
            field=models.SlugField(default=1, unique=True, verbose_name='Порядковый номер'),
            preserve_default=False,
        ),
    ]