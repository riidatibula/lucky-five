# Generated by Django 3.2.9 on 2021-12-09 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0004_lotterywinner'),
    ]

    operations = [
        migrations.AddField(
            model_name='lottery',
            name='seq',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]