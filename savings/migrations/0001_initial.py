# Generated by Django 3.0.8 on 2020-07-04 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankName', models.CharField(max_length=50)),
                ('accountName', models.CharField(max_length=50)),
                ('accountNumber', models.CharField(max_length=25)),
                ('sortCode', models.CharField(max_length=10)),
                ('predictedInterest', models.DecimalField(decimal_places=4, max_digits=6)),
                ('interestMin', models.DecimalField(decimal_places=4, max_digits=10)),
                ('interestMax', models.DecimalField(decimal_places=4, max_digits=10)),
                ('instantWithdrawal', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('balance', models.DecimalField(decimal_places=4, max_digits=10)),
                ('topup', models.DecimalField(decimal_places=4, max_digits=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='savings.Account')),
            ],
        ),
    ]
