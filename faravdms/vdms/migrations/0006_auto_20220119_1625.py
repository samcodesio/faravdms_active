# Generated by Django 3.2.8 on 2022-01-19 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vdms', '0005_auto_20220119_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_code',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_description',
            field=models.TextField(blank=True),
        ),
    ]