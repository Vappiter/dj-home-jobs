# Generated by Django 4.0.3 on 2022-11-28 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_options_alter_sensor_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='date_measurement',
            field=models.DateField(auto_now=True, verbose_name='Дата измерения'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sensor', to='measurement.sensor', verbose_name='Ссылка на датчик'),
        ),
    ]
