# Generated by Django 3.2.9 on 2022-01-14 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rba', '0051_auto_20220114_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='CSphase3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mana_meas', models.TextField(blank=True, null=True, verbose_name='3.2 Define Management Measures')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]