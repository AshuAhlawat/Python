# Generated by Django 3.0.5 on 2021-01-01 04:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='completed',
            field=models.BooleanField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
