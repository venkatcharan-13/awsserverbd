# Generated by Django 4.2.2 on 2023-06-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bloodDonateData',
            fields=[
                ('sl_no', models.BigAutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
                ('mobile_number', models.BigIntegerField(blank=True, null=True)),
                ('email_id', models.EmailField(blank=True, max_length=50, null=True)),
                ('age', models.DecimalField(decimal_places=2, max_digits=3)),
                ('gender', models.CharField(max_length=100)),
                ('blood_group', models.CharField(max_length=100)),
                ('address', models.TextField(blank=True, null=True)),
                ('upload_file', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
