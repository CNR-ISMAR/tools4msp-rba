# Generated by Django 3.1.7 on 2022-07-18 15:39

from django.db import migrations
import multiselectfield.db.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rba', '0079_futurescenarios_driven'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecoservice',
            name='relevance',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('L', 'L '), ('M', 'M'), ('H', 'H')], max_length=5, null=True, verbose_name='Overall relevance'),
        ),
        migrations.AlterField(
            model_name='futurescenarios',
            name='future_scen_desc',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='futurescenarios',
            name='relevance',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('L', 'L '), ('M', 'M'), ('H', 'H')], max_length=5, null=True, verbose_name='Overall relevance'),
        ),
        migrations.AlterField(
            model_name='phase2envs',
            name='relevance',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('L', 'L '), ('M', 'M'), ('H', 'H')], max_length=5, null=True, verbose_name='Overall relevance'),
        ),
        migrations.AlterField(
            model_name='phase2pressures',
            name='relevance',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('L', 'L '), ('M', 'M'), ('H', 'H')], max_length=5, null=True, verbose_name='Overall relevance'),
        ),
        migrations.AlterField(
            model_name='phase2uses',
            name='relevance',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('L', 'L '), ('M', 'M'), ('H', 'H')], max_length=5, null=True, verbose_name='Overall relevance'),
        ),
    ]
