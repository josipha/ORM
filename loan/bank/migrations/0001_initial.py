# Generated by Django 5.1.3 on 2024-11-12 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='loan',
            fields=[
                ('loan_id', models.IntegerField(primary_key=True, serialize=False)),
                ('loan_type', models.CharField(max_length=30)),
                ('loan_amnt', models.FloatField()),
                ('customer_acntno', models.IntegerField()),
                ('cust_name', models.CharField(max_length=50)),
            ],
        ),
    ]