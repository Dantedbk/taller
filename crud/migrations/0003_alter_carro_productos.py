# Generated by Django 4.0.5 on 2022-06-29 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_alter_carro_productos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='productos',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.producto'),
        ),
    ]
