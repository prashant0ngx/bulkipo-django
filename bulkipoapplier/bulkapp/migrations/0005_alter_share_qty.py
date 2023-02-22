# Generated by Django 3.2.17 on 2023-02-22 13:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulkapp', '0004_alter_dmatsaccount_crn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='share',
            name='qty',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(10000)]),
        ),
    ]
