# Generated by Django 3.2.9 on 2022-01-04 16:00

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rba', '0035_policyobjectives_polobj_desc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phase2envs',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='phase2envs',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='phase2envs',
            name='phase_2',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, to='rba.csphase2'),
        ),
    ]