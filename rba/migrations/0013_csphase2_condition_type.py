# Generated by Django 3.2.9 on 2021-12-13 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rba', '0012_remove_csphase2_condition_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='csphase2',
            name='condition_type',
            field=models.CharField(blank=True, choices=[('Present Condition', 'Present Condition'), ('Future Condition', 'Future Condition'), ('Management Measures', 'Management Measures')], max_length=255, null=True),
        ),
    ]
