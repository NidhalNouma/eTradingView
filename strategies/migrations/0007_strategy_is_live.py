# Generated by Django 4.2.2 on 2024-01-19 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategies', '0006_strategy_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='strategy',
            name='is_live',
            field=models.BooleanField(default=False),
        ),
    ]
