# Generated by Django 3.1.3 on 2020-11-27 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='id',
        ),
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
