# Generated by Django 3.2.3 on 2021-06-13 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=20)),
                ('writer', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('location_city', models.CharField(max_length=10)),
                ('location_detail', models.CharField(max_length=10)),
                ('rentterm', models.IntegerField()),
                ('information', models.CharField(max_length=300)),
            ],
        ),
    ]