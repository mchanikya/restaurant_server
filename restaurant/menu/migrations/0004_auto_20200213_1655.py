# Generated by Django 3.0.3 on 2020-02-13 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20200213_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='price_large',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='menu_item',
            name='price_small',
            field=models.FloatField(null=True),
        ),
    ]
