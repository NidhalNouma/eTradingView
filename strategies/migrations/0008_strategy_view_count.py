# Generated by Django 4.2.2 on 2024-01-25 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategies', '0007_strategy_is_live'),
    ]

    operations = [
        migrations.AddField(
            model_name='strategy',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
