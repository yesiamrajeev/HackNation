# Generated by Django 2.1.7 on 2019-03-20 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20190320_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dayreport',
            old_name='month',
            new_name='day',
        ),
        migrations.RenameField(
            model_name='monthreport',
            old_name='day',
            new_name='month',
        ),
    ]