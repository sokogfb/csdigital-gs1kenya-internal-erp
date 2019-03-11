# Generated by Django 2.1.5 on 2019-03-08 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0007_auto_20190308_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyleave',
            name='leave',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='leave', to='leave.Leave'),
        ),
        migrations.AlterField(
            model_name='applyleave',
            name='person_taking_charge',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='person_taking', to='accounts.Employee'),
        ),
    ]
