# Generated by Django 4.0.3 on 2022-11-24 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_rename_artticle_tag_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
    ]
