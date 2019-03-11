# Generated by Django 2.1.5 on 2019-03-11 03:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0005_auto_20190311_0318'),
        ('ACCNTS', '0004_payroll'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('payment_for', models.CharField(choices=[('Membership', 'Membership'), ('Renewal', 'Renewal'), ('Others', 'Others')], default='Membership', max_length=100)),
                ('date_of_generate', models.DateField(default=datetime.datetime.now)),
                ('VAT', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=5)),
                ('amount', models.PositiveIntegerField(blank=True, default=0)),
                ('member', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CRM.Client')),
            ],
        ),
    ]
