# Generated by Django 4.0.5 on 2022-06-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cve', '0004_remove_cve_cve_criticity_remove_cve_cve_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cve',
            name='cve_status',
            field=models.TextField(default='...'),
        ),
        migrations.AddField(
            model_name='cve',
            name='cvss',
            field=models.TextField(default='...'),
        ),
    ]
