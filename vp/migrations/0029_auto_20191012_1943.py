# Generated by Django 2.2.6 on 2019-10-12 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0028_auto_20191012_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='sweets',
            name='fm',
            field=models.CharField(default='jpg', max_length=10, verbose_name='Формат фото'),
        ),
        migrations.AddField(
            model_name='sweets',
            name='fs',
            field=models.CharField(default='jpg', max_length=10, verbose_name='Формат фото'),
        ),
        migrations.AlterField(
            model_name='sweets',
            name='sweet',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Название фото'),
        ),
    ]