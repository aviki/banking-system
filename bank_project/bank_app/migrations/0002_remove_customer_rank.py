# Generated by Django 3.2.7 on 2021-09-29 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='rank',
        ),
    ]