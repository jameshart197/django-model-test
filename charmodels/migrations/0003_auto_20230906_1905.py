# Generated by Django 3.2.21 on 2023-09-06 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charmodels', '0002_auto_20230906_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='characterdetails',
            name='age',
            field=models.CharField(blank=True, max_length=24),
        ),
        migrations.AddField(
            model_name='characterdetails',
            name='armor_class',
            field=models.CharField(blank=True, max_length=24),
        ),
        migrations.AddField(
            model_name='characterdetails',
            name='hit_points',
            field=models.CharField(blank=True, max_length=24),
        ),
        migrations.AddField(
            model_name='characterdetails',
            name='inspiration',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='characterdetails',
            name='weight',
            field=models.CharField(blank=True, max_length=24),
        ),
        migrations.AlterField(
            model_name='characterdetails',
            name='faith',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='characterdetails',
            name='height',
            field=models.CharField(blank=True, max_length=24),
        ),
    ]
