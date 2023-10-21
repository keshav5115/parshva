# Generated by Django 4.2.6 on 2023-10-21 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(max_length=100)),
                ('po_number', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('properties', models.TextField()),
            ],
        ),
    ]
