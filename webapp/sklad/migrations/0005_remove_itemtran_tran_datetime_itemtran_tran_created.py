# Generated by Django 4.0.5 on 2023-01-21 12:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sklad', '0004_itemtran_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemtran',
            name='tran_datetime',
        ),
        migrations.AddField(
            model_name='itemtran',
            name='tran_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]