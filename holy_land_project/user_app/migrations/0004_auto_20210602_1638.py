# Generated by Django 2.2.4 on 2021-06-02 13:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_auto_20210602_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Bdate',
            field=models.DateField(default=datetime.datetime(2021, 6, 2, 16, 38, 25, 872276)),
        ),
    ]
