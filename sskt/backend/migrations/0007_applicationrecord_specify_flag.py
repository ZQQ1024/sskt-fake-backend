# Generated by Django 2.1.3 on 2019-07-02 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20190701_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationrecord',
            name='specify_flag',
            field=models.IntegerField(default=0),
        ),
    ]
