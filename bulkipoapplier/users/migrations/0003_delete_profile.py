# Generated by Django 4.1.5 on 2023-01-24 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_image_profile_bio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
