# Generated by Django 3.2.9 on 2022-03-11 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('rba', '0070_csphase2_image_wmatrix'),
    ]

    operations = [
        migrations.AddField(
            model_name='csphase2',
            name='image_dmatrix',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
