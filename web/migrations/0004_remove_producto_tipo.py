# Generated by Django 5.0.6 on 2024-07-08 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_producto_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='tipo',
        ),
    ]
