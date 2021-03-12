# Generated by Django 3.1.3 on 2020-12-29 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuth', '0005_auto_20201228_2207'),
        ('settings', '0004_remove_settings_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='UserAuth.user'),
            preserve_default=False,
        ),
    ]
