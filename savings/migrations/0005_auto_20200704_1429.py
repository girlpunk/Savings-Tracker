# Generated by Django 3.0.8 on 2020-07-04 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0004_auto_20200704_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='interest_max',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='interest_min',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True),
        ),
    ]
