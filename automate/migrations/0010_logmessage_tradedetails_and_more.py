# Generated by Django 4.2.10 on 2024-12-06 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('automate', '0009_forexbrokeraccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_status', models.CharField(choices=[('E', 'Error'), ('S', 'Success')], max_length=1)),
                ('alert_message', models.TextField()),
                ('response_message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='TradeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_id', models.CharField(max_length=20)),
                ('order_id', models.CharField(max_length=20)),
                ('symbol', models.CharField(max_length=12)),
                ('volume', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('remaining_volume', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('entry_price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('exit_price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('profit', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('side', models.CharField(choices=[('B', 'Buy'), ('S', 'Sell')], max_length=1)),
                ('trade_type', models.CharField(default='S', max_length=1)),
                ('status', models.CharField(choices=[('O', 'OPEN'), ('P', 'PARTIALLY_CLOSED'), ('C', 'CLOSED')], default='O', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.RemoveField(
            model_name='cryptotradedetails',
            name='account',
        ),
        migrations.DeleteModel(
            name='CryptoLogMessage',
        ),
        migrations.DeleteModel(
            name='CryptoTradeDetails',
        ),
        migrations.AddField(
            model_name='logmessage',
            name='trade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Trade', to='automate.tradedetails'),
        ),
    ]