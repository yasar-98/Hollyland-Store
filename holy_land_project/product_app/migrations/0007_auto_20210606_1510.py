# Generated by Django 2.2.4 on 2021-06-06 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0006_auto_20210606_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
