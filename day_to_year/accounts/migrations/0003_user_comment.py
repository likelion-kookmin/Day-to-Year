# Generated by Django 3.2 on 2021-06-28 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='comment',
            field=models.CharField(blank=True, default='안녕하세요. 반갑습니다.', max_length=200, null=True),
        ),
    ]