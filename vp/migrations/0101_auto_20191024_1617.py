# Generated by Django 2.2.6 on 2019-10-24 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0100_auto_20191024_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='description',
            field=models.TextField(blank=True, db_index=True, default='', verbose_name='Краткое описание сайта'),
        ),
        migrations.AddField(
            model_name='title',
            name='header',
            field=models.CharField(db_index=True, default='', max_length=150, verbose_name='Заголовок h1 страницы сайта'),
        ),
        migrations.AlterField(
            model_name='title',
            name='title',
            field=models.CharField(db_index=True, default='', max_length=150, verbose_name='Название страницы сайта'),
        ),
    ]
