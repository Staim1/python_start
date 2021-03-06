# Generated by Django 2.1.7 on 2019-03-14 10:22

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20190314_0105'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationAlertEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_id', models.PositiveIntegerField(unique=True)),
                ('alert_ts', models.DateTimeField()),
                ('raw_data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'ordering': ['-alert_ts'],
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_ts', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.TwitchUser')),
            ],
            options={
                'ordering': ['-alert_ts'],
            },
        ),
        migrations.RemoveField(
            model_name='twitchaction',
            name='donation',
        ),
        migrations.RemoveField(
            model_name='twitchaction',
            name='user',
        ),
        migrations.AddField(
            model_name='donation',
            name='amount_usd',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='donation',
            name='source',
            field=models.CharField(choices=[('Privat24', 'Privat24'), ('Monobank', 'Monobank'), ('DonationAlert', 'DonationAlert')], default='DonationAlert', max_length=16),
        ),
        migrations.AddField(
            model_name='donation',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.TwitchUser'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='alert_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='TwitchAction',
        ),
    ]
