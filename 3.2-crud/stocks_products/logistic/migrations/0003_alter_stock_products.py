# Generated by Django 4.0.3 on 2022-12-04 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0002_alter_stock_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='products',
            field=models.ManyToManyField(related_name='stocks', through='logistic.StockProduct', to='logistic.product'),
        ),
    ]
