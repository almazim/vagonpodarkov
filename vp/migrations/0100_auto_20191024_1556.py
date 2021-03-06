# Generated by Django 2.2.6 on 2019-10-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0099_auto_20191024_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Название страницы сайта')),
            ],
            options={
                'verbose_name': 'Название страницы сайта',
                'verbose_name_plural': 'Название страницы сайта',
            },
        ),
        migrations.AlterModelOptions(
            name='main',
            options={'verbose_name': 'Шапка, логотип, фон сайта', 'verbose_name_plural': 'Шапка, логотип, фон сайта'},
        ),
        migrations.AlterField(
            model_name='classic',
            name='lists',
            field=models.ManyToManyField(blank=True, related_name='_classic_lists_+', to='vp.Sweets'),
        ),
        migrations.AlterField(
            model_name='filesload',
            name='media',
            field=models.FileField(blank=True, upload_to='files', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='main',
            name='bg',
            field=models.ImageField(blank=True, upload_to='main', verbose_name='Фон'),
        ),
        migrations.AlterField(
            model_name='main',
            name='logo',
            field=models.ImageField(blank=True, upload_to='main', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='main',
            name='main',
            field=models.ImageField(blank=True, upload_to='main', verbose_name='Шапка'),
        ),
        migrations.AlterField(
            model_name='premium',
            name='lists',
            field=models.ManyToManyField(blank=True, related_name='_premium_lists_+', to='vp.Sweets'),
        ),
    ]
