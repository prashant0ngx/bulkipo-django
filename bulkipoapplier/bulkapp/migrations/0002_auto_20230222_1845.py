# Generated by Django 3.2.17 on 2023-02-22 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulkapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dmatsaccount',
            name='crn',
            field=models.CharField(error_messages={'unique': 'A user with that db id already exists.'}, max_length=60, unique=True, verbose_name='crn'),
        ),
        migrations.AlterField(
            model_name='dmatsaccount',
            name='username',
            field=models.IntegerField(error_messages={'unique': 'A user with that db id already exists.'}, unique=True, verbose_name='username'),
        ),
    ]