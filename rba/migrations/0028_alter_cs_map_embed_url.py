# Generated by Django 3.2.9 on 2021-12-23 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rba', '0027_auto_20211223_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cs',
            name='map_embed_url',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]