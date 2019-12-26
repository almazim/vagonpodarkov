# Generated by Django 2.2.6 on 2019-10-04 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0007_auto_20191004_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer', models.TextField(blank=True, db_index=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Подвал сайта',
                'verbose_name_plural': 'Подвал сайта',
            },
        ),
        migrations.DeleteModel(
            name='Texts',
        ),
        migrations.AlterModelOptions(
            name='maintop',
            options={'verbose_name': 'Изображение в шапке сайта', 'verbose_name_plural': 'Изображение в шапке сайта'},
        ),
    ]