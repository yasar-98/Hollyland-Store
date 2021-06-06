# Generated by Django 2.2.4 on 2021-06-02 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_auto_20210602_1615'),
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='category',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(related_name='ordered_products', through='product_app.Cart', to='product_app.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ManyToManyField(related_name='user_products', through='product_app.Cart', to='user_app.User'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_carts', to='product_app.Product'),
        ),
    ]
