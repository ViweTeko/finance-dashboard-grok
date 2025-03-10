# Generated by Django 5.1.6 on 2025-02-27 08:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinancialData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('asset_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.assetclass')),
            ],
            options={
                'unique_together': {('date', 'asset_class')},
            },
        ),
    ]
