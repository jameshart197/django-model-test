# Generated by Django 3.2.21 on 2023-09-07 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charmodels', '0011_instrumentcontenttable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classlanguageproficiencies',
            name='character_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LanguagesClass', to='charmodels.classcontenttable'),
        ),
        migrations.AlterField(
            model_name='classsavingthrows',
            name='character_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SavingThrowsClass', to='charmodels.classcontenttable'),
        ),
        migrations.AlterField(
            model_name='classskillproficiencies',
            name='character_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SkillProfsClass', to='charmodels.classcontenttable'),
        ),
        migrations.AlterField(
            model_name='classspellsgranted',
            name='character_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SpellsClass', to='charmodels.classcontenttable'),
        ),
    ]
