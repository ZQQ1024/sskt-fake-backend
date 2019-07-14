# Generated by Django 2.1.8 on 2019-07-11 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recorder', models.CharField(max_length=45)),
                ('manager_number', models.CharField(default='unset', max_length=45)),
                ('updater', models.CharField(max_length=45)),
                ('lastUpdate', models.DateTimeField()),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upPerson', models.CharField(max_length=45)),
                ('createPerson', models.CharField(max_length=45)),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('updatePerson', models.CharField(max_length=45)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default='unchecked', max_length=45)),
                ('content', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('leader', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('ar', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='backend.ApplicationRecord')),
                ('managerCompanyName', models.CharField(max_length=45)),
                ('managerCompanyAddr', models.CharField(max_length=45)),
                ('managerCompanyChargerName', models.CharField(max_length=45)),
                ('managerCompanyPhone', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('ar', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='backend.ApplicationRecord')),
                ('thingName', models.CharField(max_length=45)),
                ('thingNumber', models.CharField(max_length=45)),
                ('structI', models.CharField(max_length=45)),
                ('structII', models.CharField(max_length=45)),
                ('thingArea', models.IntegerField()),
                ('stayPeopleNumber', models.IntegerField()),
                ('thingAddr', models.CharField(max_length=45)),
                ('thingAddrPostcode', models.CharField(max_length=45)),
                ('thingRentCost', models.CharField(max_length=45)),
                ('thingManageCost', models.CharField(max_length=45)),
                ('thingGiftCost', models.CharField(max_length=45)),
                ('thingDepositCost', models.CharField(max_length=45)),
                ('thingReliefCost', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Live',
            fields=[
                ('ar', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='backend.ApplicationRecord')),
                ('settlementDate', models.DateField()),
                ('contractDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('ar', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='backend.ApplicationRecord')),
                ('userNameWrite', models.CharField(max_length=45)),
                ('userNameAlias', models.CharField(max_length=45)),
                ('userNameRead', models.CharField(max_length=45)),
                ('userAddr', models.CharField(max_length=45)),
                ('userAddrPostcode', models.CharField(max_length=45)),
                ('userPhone', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('ar', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='backend.ApplicationRecord')),
                ('AD', models.CharField(max_length=45)),
                ('agencyFee', models.CharField(max_length=45)),
                ('backFee', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('ar', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='backend.ApplicationRecord')),
                ('tip', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='ar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.ApplicationRecord'),
        ),
        migrations.AddField(
            model_name='comment',
            name='ar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.ApplicationRecord'),
        ),
        migrations.AddField(
            model_name='applicationrecord',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
