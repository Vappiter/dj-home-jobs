# Generated by Django 4.0.3 on 2022-11-24 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='artticle',
            field=models.ManyToManyField(through='articles.TagArc', to='articles.article'),
        ),
    ]
