# Generated by Django 5.1.5 on 2025-01-30 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cell',
            name='is_occupied',
            field=models.BooleanField(default=False),
        ),
    ]
