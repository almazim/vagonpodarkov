# Generated by Django 2.2.6 on 2019-10-10 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0016_auto_20191010_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sweets',
            name='photos',
        ),
        migrations.AddField(
            model_name='sweets',
            name='sweet',
            field=models.ImageField(blank=True, upload_to='sweets', verbose_name='Фото'),
        ),
    ]
