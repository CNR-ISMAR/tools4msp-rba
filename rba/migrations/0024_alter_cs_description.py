# Generated by Django 3.2.9 on 2021-12-21 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rba', '0023_alter_phase2pressures_phase_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cs',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]