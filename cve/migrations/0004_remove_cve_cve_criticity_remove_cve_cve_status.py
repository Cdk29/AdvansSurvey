# Generated by Django 4.0.5 on 2022-06-24 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cve', '0003_alter_cve_cve_criticity_alter_cve_cve_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cve',
            name='cve_criticity',
        ),
        migrations.RemoveField(
            model_name='cve',
            name='cve_status',
        ),
    ]
