# Generated by Django 2.1.7 on 2019-03-14 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('BYN', 'BYN'), ('KZT', 'KZT'), ('RUB', 'RUB'), ('UAH', 'UAH'), ('BRL', 'BRL')], max_length=8)),
                ('message', models.TextField(blank=True, max_length=1024)),
                ('alert_id', models.PositiveIntegerField(unique=True)),
                ('alert_ts', models.DateTimeField()),
            ],
            options={
                'ordering': ['-alert_ts'],
            },
        ),
        migrations.CreateModel(
            name='TwitchAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribe', models.BooleanField()),
                ('alert_type', models.PositiveIntegerField()),
                ('alert_id', models.PositiveIntegerField(unique=True)),
                ('alert_ts', models.DateTimeField()),
                ('donation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.Donation')),
            ],
            options={
                'ordering': ['-alert_ts'],
            },
        ),
        migrations.CreateModel(
            name='TwitchUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('real_name', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='twitchaction',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.TwitchUser'),
        ),
    ]
