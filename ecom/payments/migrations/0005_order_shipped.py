# Generated by Django 3.2.18 on 2024-05-01 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_rename_amont_paid_order_amount_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipped',
            field=models.BooleanField(default=False),
        ),
    ]
