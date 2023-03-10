# Generated by Django 4.0.5 on 2023-01-27 20:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sklad', '0011_alter_hardware_in_use'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hardwaretype',
            options={'ordering': ['-in_use']},
        ),
        migrations.AlterModelOptions(
            name='itemforhardware',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='itemforhardware',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
