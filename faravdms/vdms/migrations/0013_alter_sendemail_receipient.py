# Generated by Django 3.2.8 on 2022-02-11 19:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vdms', '0012_alter_sendemail_receipient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendemail',
            name='receipient',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=254, null=True), blank=True, null=True, size=None), size=None),
        ),
    ]
