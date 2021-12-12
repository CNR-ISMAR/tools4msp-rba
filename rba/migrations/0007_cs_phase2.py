# Generated by Django 3.2.9 on 2021-12-12 17:25

from django.db import migrations, models
import multiselectfield.db.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rba', '0006_auto_20211207_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='CS_phase2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('condition_type', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Present Condition', 'Present Condition'), ('Future Condition', 'Future Condition'), ('Management Measures', 'Management Measures')], max_length=54, null=True)),
                ('main_pressures_effects', wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='2.3 Define main pressures / effects')),
                ('main_source_effects', wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='2.4 Describe main sources of pressures / effects')),
                ('main_environmental_responses', wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='2.5 Describe main environmental responses')),
            ],
        ),
    ]
