# Generated by Django 3.1.7 on 2022-07-15 13:11

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rba', '0078_futurescenarios_relevance'),
    ]

    operations = [
        migrations.AddField(
            model_name='futurescenarios',
            name='driven',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('BG', 'Blue Growth driven'), ('CC', 'Climate Change or Conservation driven')], max_length=5, null=True, verbose_name='Driven By'),
        ),
    ]