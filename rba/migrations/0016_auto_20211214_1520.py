# Generated by Django 3.2.9 on 2021-12-14 15:20

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rba', '0015_auto_20211214_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='csphase2',
            name='layer',
            field=models.URLField(blank=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='csphase2',
            name='pressure_description',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Describe the pressures and linkage with Marine Strategy'),
        ),
    ]