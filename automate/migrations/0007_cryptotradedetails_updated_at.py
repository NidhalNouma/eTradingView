# Generated by Django 4.2.10 on 2024-12-01 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automate', '0006_cryptotradedetails_entry_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptotradedetails',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
