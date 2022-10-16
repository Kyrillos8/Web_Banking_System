# Generated by Django 4.0.4 on 2022-05-18 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Banking_Service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('avail_bal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='transactiondetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('deb_amt', models.IntegerField()),
                ('cr_amt', models.IntegerField()),
                ('ac_bal', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Banking',
        ),
    ]
