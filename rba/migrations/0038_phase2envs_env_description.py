# Generated by Django 3.2.9 on 2022-01-04 16:25

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rba', '0037_alter_phase2envs_phase_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='phase2envs',
            name='env_description',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
