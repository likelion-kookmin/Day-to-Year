# Generated by Django 3.2.3 on 2021-06-18 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
