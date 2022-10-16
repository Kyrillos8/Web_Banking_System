# Generated by Django 4.0.4 on 2022-05-08 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banking',
            fields=[
                ('sn', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=30)),
                ('bank_name', models.CharField(max_length=20)),
                ('account_no', models.IntegerField()),
                ('Balance', models.IntegerField()),
                ('branch', models.CharField(max_length=15)),
            ],
        ),
    ]