# Generated by Django 3.2.9 on 2022-01-11 14:53

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tools4msp', '0028_auto_20211213_1143'),
        ('rba', '0043_auto_20220111_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='path_pres_env',
            name='description',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='path_use_pres',
            name='description',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.RemoveField(
            model_name='path_use_pres',
            name='use_list',
        ),
        migrations.AddField(
            model_name='path_use_pres',
            name='use_list',
            field=models.ManyToManyField(blank=True, null=True, to='tools4msp.Use'),
        ),
    ]
