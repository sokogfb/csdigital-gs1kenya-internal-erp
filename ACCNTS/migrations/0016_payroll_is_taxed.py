# Generated by Django 2.1.5 on 2019-04-17 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ACCNTS', '0015_auto_20190417_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='is_taxed',
            field=models.IntegerField(default=0),
        ),
    ]