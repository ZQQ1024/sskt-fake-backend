# Generated by Django 2.1.3 on 2019-08-18 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20190711_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='path',
            field=models.CharField(max_length=512),
        ),
    ]
