# Generated by Django 4.1.3 on 2022-11-08 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0002_car_carmodel_order_orderentry_service_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['client', 'license_plate'], 'verbose_name': 'car', 'verbose_name_plural': 'cars'},
        ),
        migrations.AlterModelOptions(
            name='carmodel',
            options={'ordering': ['maker', 'car_model'], 'verbose_name': 'car model', 'verbose_name_plural': 'car models'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['date'], 'verbose_name': 'order', 'verbose_name_plural': 'orders'},
        ),
        migrations.AlterModelOptions(
            name='orderentry',
            options={'verbose_name': 'entry of the order', 'verbose_name_plural': 'entries of the order'},
        ),
    ]
