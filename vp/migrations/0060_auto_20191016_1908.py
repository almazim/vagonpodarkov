# Generated by Django 2.2.6 on 2019-10-16 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vp', '0059_auto_20191016_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='premium',
            name='lists',
        ),
        migrations.AlterField(
            model_name='classic',
            name='lists',
            field=models.ManyToManyField(related_name='Список', to='vp.Sweets'),
        ),
        migrations.AlterField(
            model_name='classic',
            name='sweet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='vp.Sweets', verbose_name='Вид упаковки'),
        ),
    ]
