# Generated by Django 5.1.5 on 2025-01-30 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_alter_cell_is_occupied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='end_storage',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='start_storage',
            field=models.DateField(),
        ),
    ]
