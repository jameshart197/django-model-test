# Generated by Django 3.2.21 on 2023-09-06 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charmodels', '0006_spellscontenttable_spell_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='characterattributes',
            name='score',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='characterlevels',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]
