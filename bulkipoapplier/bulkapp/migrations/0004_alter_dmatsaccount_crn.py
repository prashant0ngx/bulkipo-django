# Generated by Django 3.2.17 on 2023-02-22 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulkapp', '0003_auto_20230222_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dmatsaccount',
            name='crn',
            field=models.CharField(max_length=200),
        ),
    ]