# Generated by Django 4.0.5 on 2023-01-25 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad', '0008_alter_hardware_options_alter_itemtran_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardware',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
