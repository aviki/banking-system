# Generated by Django 3.2.7 on 2021-10-04 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0006_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='transaction_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]