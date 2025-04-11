# Generated by Django 5.0.6 on 2024-07-14 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
            ],
        ),
    ]
