# Generated by Django 2.1.5 on 2019-04-23 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0010_recordapprove'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('country', models.CharField(blank=True, max_length=200)),
                ('description', models.CharField(blank=True, max_length=400)),
            ],
        ),
    ]