# Generated by Django 3.2.21 on 2023-09-06 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charmodels', '0005_auto_20230906_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='spellscontenttable',
            name='spell_level',
            field=models.IntegerField(default=1),
        ),
    ]