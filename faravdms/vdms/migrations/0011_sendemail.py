# Generated by Django 3.2.8 on 2022-02-11 19:07

import ckeditor.fields
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import vdms.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vdms', '0010_delete_sendemail'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('receipient', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=254), blank=True, null=True, size=None), size=None)),
                ('cc', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=254), blank=True, null=True, size=None), size=None)),
                ('bcc', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=254), blank=True, null=True, size=None), size=None)),
                ('message', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='files', validators=[vdms.validators.validate_file_size], verbose_name='')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
