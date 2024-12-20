# Generated by Django 4.2.10 on 2024-11-23 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile_user', '0009_alter_user_profile_lifetime_intent_and_more'),
        ('automate', '0003_remove_binanceaccount_default_symbol_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoBrokerAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('broker_type', models.CharField(choices=[('binance', 'Binance'), ('bitget', 'Bitget'), ('bybit', 'Bybit'), ('bingx', 'Bingx'), ('bitmex', 'Bitmex'), ('bitmeart', 'BitMart')], max_length=20)),
                ('type', models.CharField(choices=[('D', 'Derivatives'), ('F', 'Futures'), ('S', 'Spot'), ('U', 'USD@M'), ('C', 'COIN@M')], default='S', max_length=1)),
                ('name', models.CharField(max_length=100)),
                ('apiKey', models.CharField(max_length=150)),
                ('secretKey', models.CharField(max_length=150)),
                ('active', models.BooleanField(default=True)),
                ('pass_phrase', models.CharField(blank=True, max_length=150, null=True)),
                ('default_volume', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('custom_id', models.CharField(default='', max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_user.user_profile')),
            ],
        ),
        migrations.DeleteModel(
            name='BinanceAccount',
        ),
    ]
