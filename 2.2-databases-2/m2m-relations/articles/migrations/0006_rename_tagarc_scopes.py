# Generated by Django 4.0.3 on 2022-11-24 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_tagarc_article_alter_tagarc_tag'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TagArc',
            new_name='Scopes',
        ),
    ]
