# Generated by Django 3.2.9 on 2022-01-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rba', '0039_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csphase2',
            name='main_environmental_responses',
            field=models.TextField(blank=True, null=True, verbose_name='2.5 Describe main environmental responses'),
        ),
    ]
