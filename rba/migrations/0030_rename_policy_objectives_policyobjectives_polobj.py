# Generated by Django 3.2.9 on 2022-01-02 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rba', '0029_policyobjectives'),
    ]

    operations = [
        migrations.RenameField(
            model_name='policyobjectives',
            old_name='policy_objectives',
            new_name='polobj',
        ),
    ]