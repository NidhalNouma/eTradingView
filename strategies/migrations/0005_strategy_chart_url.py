# Generated by Django 4.2.2 on 2024-01-18 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategies', '0004_strategyresults_broker_strategyresults_gross_loss_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='strategy',
            name='chart_url',
            field=models.URLField(blank=True),
        ),
    ]
