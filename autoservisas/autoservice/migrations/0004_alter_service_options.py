# Generated by Django 4.1.3 on 2022-11-08 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0003_alter_car_options_alter_carmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['service_name'], 'verbose_name': 'service', 'verbose_name_plural': 'services'},
        ),
    ]
