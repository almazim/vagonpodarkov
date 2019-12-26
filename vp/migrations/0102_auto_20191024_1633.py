# Generated by Django 2.2.6 on 2019-10-24 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0101_auto_20191024_1617'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={'verbose_name': 'Название страницы, заголовок, краткое описание сайта', 'verbose_name_plural': 'Название страницы, заголовок, краткое описание сайта'},
        ),
        migrations.AddField(
            model_name='title',
            name='h1',
            field=models.CharField(db_index=True, default='', max_length=150, verbose_name='Заголовок h1 страницы сайта'),
        ),
        migrations.AddField(
            model_name='title',
            name='h2',
            field=models.CharField(db_index=True, default='', max_length=150, verbose_name='Заголовок h2 страницы сайта'),
        ),
        migrations.AddField(
            model_name='title',
            name='h3_classic',
            field=models.CharField(db_index=True, default='', max_length=150, verbose_name='Заголовок h3 для классики'),
        ),
        migrations.AddField(
            model_name='title',
            name='h3_premium',
            field=models.CharField(db_index=True, default='', max_length=150, verbose_name='Заголовок h3 для премиум'),
        ),
    ]