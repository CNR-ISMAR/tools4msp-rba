# Generated by Django 3.2.9 on 2022-01-20 11:46

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('rba', '0061_alter_phase2envs_env_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('doctitle', models.CharField(max_length=100, null=True)),
                ('docdesc', wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]