# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 12:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_type', models.CharField(choices=[('OW', 'One way'), ('RE', 'Rental')], max_length=2)),
                ('travel_datetime', models.DateTimeField()),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_mobile', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('0', 'Request'), ('1', 'Confirmed'), ('2', 'Declined')], max_length=1)),
                ('pnr', models.CharField(blank=True, editable=False, max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oneway_price', models.PositiveIntegerField()),
                ('driver_charge', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate_destination', to='opencabs.Place')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate_source', to='opencabs.Place')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, default='', max_length=200)),
                ('tariff_per_km', models.PositiveIntegerField()),
                ('tariff_after_hours', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, default='', max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='vehiclecategory',
            name='features',
            field=models.ManyToManyField(to='opencabs.VehicleFeature'),
        ),
        migrations.AddField(
            model_name='rate',
            name='vehicle_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rate', to='opencabs.VehicleCategory'),
        ),
        migrations.AddField(
            model_name='booking',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_destination', to='opencabs.Place'),
        ),
        migrations.AddField(
            model_name='booking',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_source', to='opencabs.Place'),
        ),
        migrations.AddField(
            model_name='booking',
            name='vehicle_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='opencabs.VehicleCategory'),
        ),
    ]
