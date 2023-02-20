# Generated by Django 3.2.17 on 2023-02-18 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DmatsAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('capital', models.IntegerField()),
                ('username', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
                ('crn', models.CharField(max_length=60)),
                ('pin', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulkapp.dmatsaccount')),
            ],
        ),
    ]
