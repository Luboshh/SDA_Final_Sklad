# Generated by Django 4.0.5 on 2023-01-25 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad', '0010_alter_hardware_created_alter_hardware_in_use'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardware',
            name='in_use',
            field=models.BooleanField(default=True),
        ),
    ]
