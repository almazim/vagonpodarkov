# Generated by Django 2.2.6 on 2019-10-20 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0088_auto_20191020_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='PremiumImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.ImageField(blank=True, upload_to='premium', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Изображения',
                'verbose_name_plural': 'Изображения подарков серии "Премиум"',
            },
        ),
        migrations.AlterField(
            model_name='premium',
            name='media',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Изображение'),
        ),
    ]
