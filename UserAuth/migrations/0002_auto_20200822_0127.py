# Generated by Django 3.0.7 on 2020-08-22 05:27

import UserAuth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='security_pin',
            field=models.CharField(default=None, max_length=20, null=True, validators=[UserAuth.validators.validate_isnumeric]),
        ),
    ]