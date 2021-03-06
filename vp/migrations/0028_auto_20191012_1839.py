# Generated by Django 2.2.6 on 2019-10-12 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0027_auto_20191012_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Название')),
                ('sweet', models.CharField(db_index=True, max_length=150, verbose_name='Фото')),
                ('descript', models.TextField(blank=True, db_index=True, verbose_name='Описание')),
                ('manufact', models.CharField(db_index=True, max_length=150, verbose_name='Производитель')),
                ('counts', models.IntegerField(blank=True, default=1, verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Список сладостей',
                'verbose_name_plural': 'Сладости',
            },
        ),
        migrations.RemoveField(
            model_name='classic',
            name='counts',
        ),
        migrations.RemoveField(
            model_name='classic',
            name='description',
        ),
        migrations.RemoveField(
            model_name='classic',
            name='manufactures',
        ),
        migrations.RemoveField(
            model_name='classic',
            name='sweets',
        ),
        migrations.RemoveField(
            model_name='premium',
            name='counts',
        ),
        migrations.RemoveField(
            model_name='premium',
            name='description',
        ),
        migrations.RemoveField(
            model_name='premium',
            name='manufactures',
        ),
        migrations.RemoveField(
            model_name='premium',
            name='sweets',
        ),
        migrations.AlterField(
            model_name='classic',
            name='names',
            field=models.TextField(blank=True, db_index=True, verbose_name='Названия сладостей подарка (через запятую)'),
        ),
        migrations.AlterField(
            model_name='premium',
            name='names',
            field=models.TextField(blank=True, db_index=True, verbose_name='Названия сладостей подарка (через запятую)'),
        ),
    ]
