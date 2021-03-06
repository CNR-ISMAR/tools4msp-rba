# Generated by Django 3.2.9 on 2022-01-17 11:05

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rba', '0054_managementmeasures'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cs',
            name='es_type',
        ),
        migrations.CreateModel(
            name='EcoService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('es_type', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Habitat Maintenance', 'Habitat Maintenance'), ('Carbon Sequestration', 'Carbon Sequestration'), ('Food provision', 'Food provision'), ('Water Quality', 'Water Quality'), ('Fish Migration Route', 'Fish Migration Route'), ('Buffering Against Anoxia', 'Buffering Against Anoxia'), ('Recreation and Tourism', 'Recreation and Tourism'), ('Climate Regulation', 'Climate Regulation')], max_length=157, null=True)),
                ('ecoobj', models.TextField(blank=True, null=True, verbose_name='Ecosystem Service')),
                ('ecoobj_desc', models.TextField(blank=True, null=True, verbose_name='Ecosystem Service Description')),
                ('phase_1', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='eco_objects', to='rba.cs')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
