# Generated by Django 5.2.4 on 2025-07-17 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_details_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='phone_no',
            field=models.BigIntegerField(),
        ),
    ]
