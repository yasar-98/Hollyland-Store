# Generated by Django 2.2.4 on 2021-06-05 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_auto_20210602_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Bdate',
            field=models.DateField(default=datetime.datetime(2021, 6, 5, 22, 42, 32, 964989)),
        ),
    ]
