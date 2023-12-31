# Generated by Django 3.2.21 on 2023-09-07 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charmodels', '0009_auto_20230906_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spellscontenttable',
            name='spell_level',
            field=models.IntegerField(choices=[(0, 'Cantrip'), (1, '1st'), (2, '2nd'), (3, '3rd'), (4, '4th'), (5, '5th'), (6, '6th'), (7, '7th'), (8, '8th'), (9, '9th')], default=0),
        ),
        migrations.AlterField(
            model_name='subclasscontenttable',
            name='parent_class',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='SubclassParentClass', to='charmodels.classcontenttable'),
        ),
    ]
