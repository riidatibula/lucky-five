# Generated by Django 3.2.9 on 2021-11-16 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LuckyFive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=5)),
                ('signature', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Lottery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('number', models.PositiveIntegerField()),
                ('date', models.DateTimeField()),
                ('policy_id', models.CharField(max_length=250)),
                ('lucky_five', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lottery.luckyfive')),
            ],
        ),
        migrations.CreateModel(
            name='Bet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bettor', models.CharField(blank=True, max_length=250, null=True)),
                ('payment_address', models.CharField(max_length=250)),
                ('is_active', models.BooleanField(default=False)),
                ('lucky_five', models.CharField(max_length=5)),
                ('ticket', models.CharField(blank=True, max_length=250, null=True)),
                ('lottery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lottery.lottery')),
            ],
        ),
    ]
