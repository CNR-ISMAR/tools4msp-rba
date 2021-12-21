# Generated by Django 3.2.9 on 2021-12-13 16:49

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rba', '0013_csphase2_condition_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csphase2',
            name='condition_type',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Present Condition', 'Present Condition'), ('Future Condition', 'Future Condition'), ('Management Measures', 'Management Measures')], max_length=54, null=True),
        ),
    ]