# Generated by Django 3.2.21 on 2023-09-07 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charmodels', '0010_auto_20230907_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstrumentContentTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('full_description', models.CharField(max_length=10000)),
            ],
            options={
                'verbose_name': 'Musical Instrument',
            },
        ),
    ]
