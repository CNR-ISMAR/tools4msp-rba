# Generated by Django 3.1.7 on 2022-07-15 12:42

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rba', '0077_ecoservice_relevance'),
    ]

    operations = [
        migrations.AddField(
            model_name='futurescenarios',
            name='relevance',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], max_length=5, null=True, verbose_name='Overall relevance'),
        ),
    ]
