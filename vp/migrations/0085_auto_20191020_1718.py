# Generated by Django 2.2.6 on 2019-10-20 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0084_auto_20191020_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sweets',
            name='number',
            field=models.CharField(db_index=True, max_length=10, verbose_name='Номер подарка'),
        ),
    ]
