# Generated by Django 2.2.6 on 2019-10-14 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0029_auto_20191012_1943'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sweets',
            options={'verbose_name': 'id Список сладостей', 'verbose_name_plural': 'Сладости'},
        ),
        migrations.RemoveField(
            model_name='classic',
            name='names',
        ),
        migrations.RemoveField(
            model_name='premium',
            name='names',
        ),
        migrations.AddField(
            model_name='sweets',
            name='slug',
            field=models.SlugField(default=0, unique=True, verbose_name='Порядковый номер'),
        ),
    ]
