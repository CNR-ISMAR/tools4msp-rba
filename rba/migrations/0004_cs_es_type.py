# Generated by Django 3.2.9 on 2021-12-02 09:56

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rba', '0003_cs_map_embed_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='cs',
            name='es_type',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Monitoring program', 'Monitoring program'), ('Portal', 'Portal'), ('Map', 'Map'), ('Dataset', 'Dataset'), ('Data Source', 'Data Source'), ('Other', 'Other')], max_length=55, null=True),
        ),
    ]
