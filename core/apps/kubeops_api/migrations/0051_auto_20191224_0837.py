# Generated by Django 2.1.15 on 2019-12-24 08:37

import common.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kubeops_api', '0050_auto_20191224_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='info',
            field=common.models.JsonDictTextField(default={}),
        ),
        migrations.AlterField(
            model_name='clusterhealthhistory',
            name='date_type',
            field=models.CharField(choices=[('DAY', 'DAY'), ('HOUR', 'HOUR')], default='HOUR', max_length=255),
        ),
    ]